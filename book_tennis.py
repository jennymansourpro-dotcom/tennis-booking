#!/usr/bin/env python3
"""Réservation automatique d'un créneau de tennis sur tennis.paris.fr.

Cible fixe (pilotée par variables d'environnement, aucun identifiant en dur) :
  - site : Tennis Edouard Pailleron (19ème arrondissement)
  - créneau : mercredi 19h, court 2
  - ouverture des réservations : 08:00:00 heure de Paris

Sorties dans out/ :
  - result.json (status: booked | dry_run | not_found | error)
  - captures d'écran + dumps HTML numérotés à chaque étape (01_landing … 99_error)

Le mot de passe n'est JAMAIS écrit dans les logs ni dans result.json.
"""

import json
import os
import re
import sys
import time
import traceback
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from playwright.sync_api import TimeoutError as PWTimeoutError
from playwright.sync_api import sync_playwright

load_dotenv()

PARIS_TZ = ZoneInfo("Europe/Paris")
OUT_DIR = Path(__file__).resolve().parent / "out"

SEARCH_URL = (
    "https://tennis.paris.fr/tennis/jsp/site/Portal.jsp"
    "?page=recherche&view=recherche_creneau"
)

FRENCH_DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
FRENCH_MONTHS = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre",
]


def env(name, default=None):
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


def env_flag(name):
    return env(name, "0").strip().lower() in ("1", "true", "yes", "on")


class Config:
    def __init__(self):
        self.email = env("PARIS_TENNIS_EMAIL")
        self.password = env("PARIS_TENNIS_PASSWORD")
        self.partner_firstname = env("TENNIS_PARTNER_FIRSTNAME", "Mehdi")
        self.partner_lastname = env("TENNIS_PARTNER_LASTNAME", "Kellal")
        self.site_name = env("TENNIS_SITE_NAME", "Edouard Pailleron")
        self.arrondissement = int(env("TENNIS_ARRONDISSEMENT", "19"))
        self.court = int(env("TENNIS_COURT", "2"))
        self.start_hour = int(env("TENNIS_START_HOUR", "19"))
        self.weekday = int(env("TENNIS_WEEKDAY", "2"))  # 0=lundi … 2=mercredi
        self.open_at = env("TENNIS_OPEN_AT", "08:00:00")
        self.deadline_minutes = float(env("TENNIS_DEADLINE_MINUTES", "6"))
        self.dry_run = env_flag("DRY_RUN")
        self.skip_wait = env_flag("SKIP_WAIT")

        if not self.email or not self.password:
            raise SystemExit(
                "PARIS_TENNIS_EMAIL et PARIS_TENNIS_PASSWORD doivent être définis "
                "(variables d'environnement ou .env)."
            )

    def target_date(self):
        """Prochain jour `weekday` strictement après aujourd'hui (heure de Paris)."""
        today = datetime.now(PARIS_TZ).date()
        delta = (self.weekday - today.weekday()) % 7
        if delta == 0:
            delta = 7
        return today + timedelta(days=delta)


def log(message):
    stamp = datetime.now(PARIS_TZ).strftime("%H:%M:%S.%f")[:-3]
    print(f"[{stamp}] {message}", flush=True)


class Recorder:
    """Capture d'écran + dump HTML à chaque étape, dans out/."""

    def __init__(self, page):
        self.page = page

    def snap(self, name):
        try:
            self.page.screenshot(path=str(OUT_DIR / f"{name}.png"), full_page=True)
        except Exception as exc:  # la capture ne doit jamais faire échouer le run
            log(f"capture {name} impossible: {type(exc).__name__}")
        try:
            (OUT_DIR / f"{name}.html").write_text(self.page.content(), encoding="utf-8")
        except Exception as exc:
            log(f"dump {name} impossible: {type(exc).__name__}")
        log(f"étape enregistrée: {name}")


def write_result(status, cfg, target, reason=None):
    start = datetime(target.year, target.month, target.day, cfg.start_hour, 0, tzinfo=PARIS_TZ)
    end = start + timedelta(hours=1)
    result = {
        "status": status,
        "target_date": target.isoformat(),
        "start_iso": start.isoformat(),
        "end_iso": end.isoformat(),
        "court": cfg.court,
        "site": f"Tennis {cfg.site_name}",
        "arrondissement": cfg.arrondissement,
        "partner": f"{cfg.partner_firstname} {cfg.partner_lastname}",
        "reason": reason,
    }
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    log(f"result.json écrit: status={status}" + (f" reason={reason}" if reason else ""))
    return result


def first_visible(candidates, timeout=2000):
    """Retourne le premier locator visible parmi une liste de stratégies."""
    for locator in candidates:
        try:
            target = locator.first
            target.wait_for(state="visible", timeout=timeout)
            return target
        except Exception:
            continue
    return None


def click_first(page, candidates, description, timeout=4000):
    target = first_visible(candidates, timeout=timeout)
    if target is None:
        raise RuntimeError(f"Élément introuvable: {description}")
    target.scroll_into_view_if_needed()
    target.click()
    log(f"clic: {description}")
    page.wait_for_load_state("domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=8000)
    except PWTimeoutError:
        pass
    return target


def login(page, rec, cfg):
    log("ouverture de la page de recherche (redirection SSO attendue)")
    page.goto(SEARCH_URL, wait_until="domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=15000)
    except PWTimeoutError:
        pass
    rec.snap("01_landing")

    # Bandeau cookies éventuel (paris.fr utilise souvent un bouton de refus/accept).
    for pattern in (r"tout refuser", r"continuer sans accepter", r"tout accepter", r"^accepter"):
        try:
            page.get_by_role("button", name=re.compile(pattern, re.I)).first.click(timeout=1500)
            log(f"bandeau cookies fermé ({pattern})")
            break
        except Exception:
            continue

    # Si nous ne sommes pas déjà sur le formulaire Keycloak, déclencher la connexion.
    if not page.locator("#username").first.is_visible():
        connect = first_visible(
            [
                page.locator("a.banner-mon-compte__connexion-avatar"),
                page.get_by_role("link", name=re.compile(r"s'authentifier|connexion|se connecter", re.I)),
                page.locator("a[href*='DoMyLuteceLogin']"),
            ],
            timeout=3000,
        )
        if connect is not None:
            connect.click()
            page.wait_for_load_state("domcontentloaded")
        if not page.locator("#username").first.is_visible():
            # Repli fiable : l'URL de connexion MyLutece redirige vers le SSO Keycloak.
            page.goto(
                "https://tennis.paris.fr/tennis/jsp/site/plugins/mylutece/DoMyLuteceLogin.jsp",
                wait_until="domcontentloaded",
            )

    page.locator("#username").wait_for(state="visible", timeout=20000)
    if "auth.paris.fr" not in page.url:
        log(f"attention: formulaire de connexion sur un domaine inattendu: {page.url}")
    rec.snap("02_login_form")

    page.locator("#username").fill(cfg.email)
    page.locator("#password").fill(cfg.password)
    log(f"identifiants saisis pour {cfg.email} (mot de passe masqué)")
    submit = first_visible(
        [
            page.locator("#kc-login"),
            page.locator("form#form-login button[type='submit']"),
            page.locator("form button[type='submit'][name='Submit']"),
            page.get_by_role("button", name=re.compile(r"se connecter|connexion|valider", re.I)),
        ],
        timeout=5000,
    )
    if submit is None:
        raise RuntimeError("Bouton de soumission du formulaire de connexion introuvable")
    submit.click()
    page.wait_for_load_state("domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=20000)
    except PWTimeoutError:
        pass

    if page.locator("#username").first.is_visible() or page.locator(
        ".alert-error, #input-error, .kc-feedback-text"
    ).first.is_visible():
        rec.snap("99_error")
        raise RuntimeError("Échec de connexion SSO: le formulaire est toujours affiché.")
    rec.snap("03_logged_in")


def goto_planning(page, rec, cfg):
    """Depuis l'accueil connecté : Paris Tennis → Tennis parisiens →
    arrondissement → site → planning."""

    # (1) "Paris Tennis" dans « mes services favoris »
    try:
        click_first(
            page,
            [
                page.get_by_role("link", name=re.compile(r"paris\s*tennis", re.I)),
                page.get_by_text(re.compile(r"paris\s*tennis", re.I)),
            ],
            "Paris Tennis (mes services favoris)",
            timeout=6000,
        )
    except RuntimeError:
        # Repli : aller directement sur la page de recherche de créneau.
        log("lien 'Paris Tennis' introuvable, accès direct à la page de recherche")
        page.goto(SEARCH_URL, wait_until="domcontentloaded")
    rec.snap("04_paris_tennis")

    # (2) "Tennis parisiens"
    try:
        click_first(
            page,
            [
                page.get_by_role("link", name=re.compile(r"tennis\s+parisiens", re.I)),
                page.get_by_role("button", name=re.compile(r"tennis\s+parisiens", re.I)),
                page.get_by_text(re.compile(r"tennis\s+parisiens", re.I)),
            ],
            "Tennis parisiens",
            timeout=6000,
        )
    except RuntimeError:
        log("entrée 'Tennis parisiens' non trouvée, on continue (peut-être déjà sur la liste)")
    rec.snap("05_tennis_parisiens")

    # (3) Menu de l'arrondissement, ex. « 19ème arrondissement »
    arr = cfg.arrondissement
    arr_pattern = re.compile(rf"\b{arr}\s*(er|e|ème|eme)?\b.*arrondissement", re.I)
    arr_click = first_visible(
        [
            page.get_by_role("link", name=arr_pattern),
            page.get_by_role("button", name=arr_pattern),
            page.get_by_text(arr_pattern),
        ],
        timeout=4000,
    )
    if arr_click is None:
        # Certains menus sont repliés : tenter d'ouvrir un accordéon/menu générique.
        toggles = page.get_by_role("button", name=re.compile(r"arrondissement", re.I))
        try:
            toggles.first.click(timeout=2000)
        except Exception:
            pass
        arr_click = first_visible(
            [page.get_by_text(arr_pattern), page.locator(f"[data-arrondissement='{arr}']")],
            timeout=4000,
        )
    if arr_click is None:
        raise RuntimeError(f"Menu de l'arrondissement {arr} introuvable")
    arr_click.click()
    page.wait_for_load_state("domcontentloaded")
    rec.snap("06_arrondissement")

    # (4) Le site, ex. « Tennis Edouard Pailleron » — cliquer « Voir la fiche »
    # dans la ligne du tableau qui porte le nom du site.
    site_pattern = re.compile(re.escape(cfg.site_name), re.I)
    site_row = page.locator("tr", has_text=site_pattern)
    click_first(
        page,
        [
            site_row.get_by_role("link", name=re.compile(r"voir la fiche", re.I)),
            site_row.locator("a", has_text=re.compile(r"voir la fiche", re.I)),
            page.get_by_role("link", name=site_pattern),
            page.get_by_text(site_pattern),
        ],
        f"site « {cfg.site_name} »",
        timeout=8000,
    )
    rec.snap("07_site")

    # (5) « Voir le planning du tennis »
    try:
        click_first(
            page,
            [
                page.get_by_role("link", name=re.compile(r"voir le planning", re.I)),
                page.get_by_role("button", name=re.compile(r"voir le planning", re.I)),
                page.get_by_text(re.compile(r"voir le planning", re.I)),
            ],
            "Voir le planning du tennis",
            timeout=6000,
        )
    except RuntimeError:
        log("bouton 'Voir le planning' non trouvé, le planning est peut-être déjà affiché")
    rec.snap("08_planning")


def select_day(page, rec, cfg, target):
    """Sélectionne le jour cible dans le planning (onglets ou navigation par flèches)."""
    day_label = f"{FRENCH_DAYS[target.weekday()]} {target.day:02d}"
    patterns = [
        re.compile(rf"{FRENCH_DAYS[target.weekday()]}\s*0?{target.day}\b", re.I),
        re.compile(rf"\b0?{target.day}\s+{FRENCH_MONTHS[target.month - 1]}", re.I),
        re.compile(rf"{target.day:02d}/{target.month:02d}"),
    ]

    for attempt in range(10):
        for pattern in patterns:
            tab = first_visible(
                [
                    page.get_by_role("tab", name=pattern),
                    page.get_by_role("link", name=pattern),
                    page.get_by_role("button", name=pattern),
                    page.get_by_text(pattern),
                ],
                timeout=1500,
            )
            if tab is not None:
                tab.click()
                page.wait_for_load_state("domcontentloaded")
                try:
                    page.wait_for_load_state("networkidle", timeout=6000)
                except PWTimeoutError:
                    pass
                log(f"jour sélectionné: {day_label}")
                rec.snap("09_day_selected")
                return
        # Jour non visible : avancer d'un écran de jours si possible.
        forward = first_visible(
            [
                page.get_by_role("button", name=re.compile(r"suivant|next|›|>", re.I)),
                page.locator("[class*='next']"),
            ],
            timeout=1500,
        )
        if forward is None:
            break
        forward.click()
        page.wait_for_timeout(700)

    rec.snap("09_day_selected")
    raise RuntimeError(f"Jour cible « {day_label} » introuvable dans le planning")


def run_search(page, cfg, target):
    """Depuis la page de recherche, remplit « Où ? » + date puis lance la recherche.

    La réservation ne passe pas par le planning hebdomadaire (informatif) mais par
    ce formulaire : les résultats listent, par heure, les courts libres avec un
    bouton « Réserver » portant les attributs equipmentid/courtid/datedeb.
    """
    page.goto(SEARCH_URL, wait_until="domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except PWTimeoutError:
        pass

    # Champ « Où ? » : widget d'autocomplétion à tokens.
    token_input = page.locator("#whereToken .tokens-input-text")
    token_input.wait_for(state="visible", timeout=10000)
    token_input.click()
    token_input.type(cfg.site_name, delay=40)
    suggestion = page.locator(
        ".tokens-suggestion-selector li.tokens-suggestions-list-element",
        has_text=re.compile(re.escape(cfg.site_name), re.I),
    ).first
    suggestion.wait_for(state="visible", timeout=8000)
    suggestion.click(force=True)

    # Champ « Quand ? » : ouvrir le date-picker et choisir le jour cible.
    date_iso = target.strftime("%d/%m/%Y")
    page.locator("#when").click()
    day_item = page.locator(f".date-picker .date[dateiso='{date_iso}']")
    day_item.first.wait_for(state="visible", timeout=5000)
    day_item.first.click()

    page.locator("#rechercher").click()
    page.wait_for_load_state("domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except PWTimeoutError:
        pass


def find_slot(page, cfg, target):
    """Sur la page de résultats, déplie le panneau de l'heure cible et retourne
    le bouton « Réserver » du court cible, ou None."""
    hour_label = f"{cfg.start_hour:02d}h"
    court_re = re.compile(rf"court\s*n?[°o]?\s*0*{cfg.court}\b", re.I)
    datedeb = f"{target.strftime('%Y/%m/%d')} {cfg.start_hour:02d}:00:00"

    # Déplier l'accordéon de l'heure cible s'il n'est pas déjà ouvert.
    try:
        panel_link = page.locator(
            ".panel a", has=page.locator(".panel-title", has_text=re.compile(rf"^\s*{hour_label}\s*$"))
        ).first
        if panel_link.count() and panel_link.get_attribute("aria-expanded") != "true":
            panel_link.click()
            page.wait_for_timeout(600)
    except Exception:
        pass

    # Stratégie A : bouton avec l'attribut datedeb exact, dans la ligne du bon court.
    try:
        row = page.locator("div.tennis-court", has_text=court_re)
        button = row.locator(f"button.buttonAllOk[datedeb='{datedeb}']").first
        if button.count() and button.is_visible() and button.is_enabled():
            return button
    except Exception:
        pass

    # Stratégie B : n'importe quel bouton Réserver du bon datedeb dont la ligne
    # parente mentionne le bon court.
    try:
        buttons = page.locator(f"button[datedeb='{datedeb}']")
        for i in range(buttons.count()):
            item = buttons.nth(i)
            row_text = item.locator(
                "xpath=ancestor::div[contains(@class,'tennis-court')]"
            ).inner_text(timeout=800)
            if court_re.search(row_text) and item.is_visible():
                return item
    except Exception:
        pass

    # Stratégie C : bouton/lien « Réserver » générique dans une ligne heure+court.
    try:
        hour_re = re.compile(rf"\b{cfg.start_hour}\s*h(?:00)?\b", re.I)
        candidates = page.get_by_role("button", name=re.compile(r"réserver", re.I))
        for i in range(candidates.count()):
            item = candidates.nth(i)
            blob = " ".join(
                filter(None, [item.get_attribute("datedeb"), item.get_attribute("title")])
            )
            try:
                blob += " " + item.locator("xpath=ancestor::div[2]").inner_text(timeout=500)
            except Exception:
                pass
            if hour_re.search(blob) and court_re.search(blob) and item.is_visible():
                return item
    except Exception:
        pass

    return None


def wait_for_opening(page, rec, cfg):
    """Attend 08:00:00.000 heure de Paris en gardant la session vivante (reload/60 s)."""
    open_h, open_m, open_s = (int(x) for x in cfg.open_at.split(":"))
    now = datetime.now(PARIS_TZ)
    open_dt = now.replace(hour=open_h, minute=open_m, second=open_s, microsecond=0)
    if now >= open_dt:
        log("heure d'ouverture déjà passée, pas d'attente")
        return
    log(f"attente jusqu'à {open_dt.isoformat()} (reload de maintien toutes les 60 s)")
    while True:
        now = datetime.now(PARIS_TZ)
        remaining = (open_dt - now).total_seconds()
        if remaining <= 0:
            break
        if remaining > 61:
            time.sleep(min(60, remaining - 1))
            try:
                page.reload(wait_until="domcontentloaded")
                log(f"session maintenue, reste {int((open_dt - datetime.now(PARIS_TZ)).total_seconds())} s")
            except Exception as exc:
                log(f"reload de maintien en échec ({type(exc).__name__}), on continue")
        else:
            # Dernière minute : attente fine sans reload pour partir pile à l'heure.
            time.sleep(min(0.05, max(remaining, 0.001)))
    log("top départ: heure d'ouverture atteinte")


def hunt_slot(page, rec, cfg, target):
    """Relance la recherche toutes les ~1,5 s jusqu'à trouver le créneau,
    au plus deadline_minutes."""
    deadline = time.monotonic() + cfg.deadline_minutes * 60
    attempt = 0
    while time.monotonic() < deadline:
        attempt += 1
        try:
            run_search(page, cfg, target)
        except Exception as exc:
            log(f"recherche en échec ({type(exc).__name__}), nouvel essai")
            time.sleep(1.5)
            continue
        slot = find_slot(page, cfg, target)
        if slot is not None:
            log(f"créneau {cfg.start_hour}h / court {cfg.court} trouvé (essai {attempt})")
            return slot
        if cfg.skip_wait and attempt >= 2:
            # En mode calage on ne boucle pas 6 minutes pour rien.
            log("SKIP_WAIT actif: arrêt de la recherche après 2 essais")
            return None
        time.sleep(1.5)
    log("délai de recherche du créneau dépassé")
    return None


class CaptchaRequired(RuntimeError):
    pass


def check_captcha(page):
    """Le site affiche un captcha anti-robot après le clic « Réserver ».

    On ne tente JAMAIS de le contourner : on échoue proprement pour que la
    routine envoie le mail d'échec avec la capture.
    """
    body = ""
    try:
        body = page.locator("body").inner_text(timeout=3000)
    except Exception:
        pass
    if re.search(r"captcha|vérification de sécurité|bloquons les robots", body, re.I):
        raise CaptchaRequired(
            "Captcha anti-robot affiché après le clic Réserver — réservation "
            "automatique impossible, intervention humaine requise."
        )


AMOUNT_RE = re.compile(r"(\d+(?:[.,]\d{1,2})?)\s*(?:€|euros?\b)", re.I)


def assert_free_of_charge(page):
    """Interdit de continuer si un montant non nul en euros est affiché."""
    text = page.locator("body").inner_text(timeout=5000)
    for match in AMOUNT_RE.finditer(text):
        value = float(match.group(1).replace(",", "."))
        if value > 0:
            raise RuntimeError(
                f"Montant non nul affiché ({match.group(0).strip()}) — réservation refusée."
            )


def fill_partner_and_confirm(page, rec, cfg):
    """Renseigne le partenaire puis enchaîne les écrans Confirmer/Valider."""
    firstname_candidates = [
        page.get_by_label(re.compile(r"pr[ée]nom", re.I)),
        page.locator("input[name*='firstname' i], input[id*='firstname' i]"),
        page.locator("input[name*='prenom' i], input[id*='prenom' i]"),
    ]
    lastname_candidates = [
        page.get_by_label(re.compile(r"^nom|nom du (joueur|partenaire)", re.I)),
        page.locator("input[name*='lastname' i], input[id*='lastname' i]"),
        page.locator("input[name*='nom' i]:not([name*='prenom' i]), "
                     "input[id*='nom' i]:not([id*='prenom' i])"),
    ]

    first_input = first_visible(firstname_candidates, timeout=8000)
    last_input = first_visible(lastname_candidates, timeout=8000)
    if first_input is None or last_input is None:
        raise RuntimeError("Champs prénom/nom du partenaire introuvables")

    first_input.fill(cfg.partner_firstname)
    last_input.fill(cfg.partner_lastname)
    log(f"partenaire renseigné: {cfg.partner_firstname} {cfg.partner_lastname}")
    rec.snap("10_partner_filled")

    if cfg.dry_run:
        log("DRY_RUN=1 → arrêt avant toute validation")
        return "dry_run"

    assert_free_of_charge(page)

    # Écrans Confirmer / Valider successifs (au plus 4 pour éviter une boucle infinie).
    for step in range(4):
        assert_free_of_charge(page)
        button = first_visible(
            [
                page.get_by_role("button", name=re.compile(r"confirmer|valider|réserver", re.I)),
                page.get_by_role("link", name=re.compile(r"confirmer|valider|réserver", re.I)),
                page.locator("input[type='submit']"),
            ],
            timeout=5000,
        )
        if button is None:
            break
        label = ""
        try:
            label = button.inner_text(timeout=500)
        except Exception:
            pass
        button.click()
        log(f"validation {step + 1}: bouton « {label.strip() or 'submit'} » cliqué")
        page.wait_for_load_state("domcontentloaded")
        try:
            page.wait_for_load_state("networkidle", timeout=8000)
        except PWTimeoutError:
            pass
        rec.snap(f"11_confirm_{step + 1}")
        body = page.locator("body").inner_text(timeout=5000)
        if re.search(r"réservation (est )?(confirmée|enregistrée|validée)", body, re.I):
            log("confirmation de réservation détectée")
            return "booked"
    return "booked"


def main():
    cfg = Config()
    target = cfg.target_date()
    OUT_DIR.mkdir(exist_ok=True)
    log(
        f"cible: {FRENCH_DAYS[target.weekday()]} {target.isoformat()} "
        f"{cfg.start_hour}h court {cfg.court} @ Tennis {cfg.site_name} "
        f"({cfg.arrondissement}e) — dry_run={cfg.dry_run} skip_wait={cfg.skip_wait}"
    )

    with sync_playwright() as pw:
        # Respecter un éventuel proxy d'egress (ex: environnement cloud Claude Code).
        # Contraintes du proxy TLS d'inspection : il ne comprend ni le mode
        # headless "old" de Chromium ni son ClientHello TLS 1.3 — on force le
        # nouveau mode headless et on plafonne à TLS 1.2 vers le proxy local
        # (qui re-chiffre lui-même vers l'origine). Vérification TLS inchangée.
        proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
        if proxy_url:
            launch_kwargs = {
                "headless": False,
                "proxy": {"server": proxy_url},
                "args": ["--headless=new", "--ssl-version-max=tls1.2"],
            }
        else:
            launch_kwargs = {"headless": True}
        browser = pw.chromium.launch(**launch_kwargs)
        context = browser.new_context(
            locale="fr-FR",
            timezone_id="Europe/Paris",
            viewport={"width": 1440, "height": 1000},
        )
        page = context.new_page()
        page.set_default_timeout(15000)
        rec = Recorder(page)

        try:
            login(page, rec, cfg)
            goto_planning(page, rec, cfg)
            select_day(page, rec, cfg, target)

            if not cfg.skip_wait:
                wait_for_opening(page, rec, cfg)

            slot = hunt_slot(page, rec, cfg, target)
            if slot is None:
                rec.snap("99_error")
                write_result(
                    "not_found", cfg, target,
                    reason=f"créneau {cfg.start_hour}h / court {cfg.court} jamais cliquable "
                           f"dans le délai de {cfg.deadline_minutes} min",
                )
                return 1

            slot.scroll_into_view_if_needed()
            slot.click()
            page.wait_for_load_state("domcontentloaded")
            try:
                page.wait_for_load_state("networkidle", timeout=8000)
            except PWTimeoutError:
                pass
            rec.snap("09b_slot_clicked")

            check_captcha(page)

            status = fill_partner_and_confirm(page, rec, cfg)
            write_result(status, cfg, target)
            return 0
        except Exception as exc:
            reason = str(exc)
            # Ceinture et bretelles : jamais le mot de passe dans les sorties.
            if cfg.password:
                reason = reason.replace(cfg.password, "***")
            log(f"ERREUR: {type(exc).__name__}: {reason}")
            traceback.print_exc()
            try:
                rec.snap("99_error")
            except Exception:
                pass
            write_result("error", cfg, target, reason=f"{type(exc).__name__}: {reason}")
            return 1
        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    sys.exit(main())
