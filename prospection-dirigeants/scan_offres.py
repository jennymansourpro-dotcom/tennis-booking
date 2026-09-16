# -*- coding: utf-8 -*-
"""Recherche les offres d'emploi ouvertes chez les entreprises cibles.

Source principale : les API publiques des ATS utilisés par les pages carrières
(Ashby, Greenhouse, Lever, Recruitee, SmartRecruiters, Teamtailor, Workable).
C'est la seule source stable : Welcome to the Jungle, LinkedIn Jobs et Indeed
placent leurs listes derrière une authentification ou un anti-robot, et leurs
conditions d'utilisation interdisent l'extraction automatisée. Les offres
publiées sur ces sites sont récupérées autrement, par le moteur de recherche,
dans l'étape 2 de la routine (voir ROUTINE_OFFRES_PROMPT.md).

Usage : python scan_offres.py [--tout] [--cache]
Sortie : out/offres.json
"""

import argparse
import concurrent.futures as futures
import importlib.util
import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from datetime import datetime, timezone

ICI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(ICI, "out", "cache_ats")
UA = "Mozilla/5.0 (compatible; veille-emploi/1.0)"
DELAI = 15

ATS = {
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{slug}",
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true",
    "lever": "https://api.lever.co/v0/postings/{slug}?mode=json",
    "recruitee": "https://{slug}.recruitee.com/api/offers/",
    "smartrecruiters": "https://api.smartrecruiters.com/v1/companies/{slug}/postings?limit=100",
    "teamtailor": "https://{slug}.teamtailor.com/jobs.json",
    "workable": "https://apply.workable.com/api/v1/widget/accounts/{slug}?details=true",
    "personio": "https://{slug}.jobs.personio.de/search.json",
    "join": "https://join.com/api/public/companies/{slug}/jobs",
}

# Slugs qui ne se déduisent pas du nom de l'entreprise. À compléter au fil des
# exécutions : c'est ce qui fait progresser la couverture d'une semaine sur l'autre.
SLUGS_CONNUS = {
    "Huwise (ex-Opendatasoft)": ["opendatasoft", "huwise"],
    "Unowhy (SQOOL)": ["Unowhy", "unowhy"],
    "Sinequa (ChapsVision)": ["sinequa", "chapsvision"],
    "Miralia (ex-Golem.ai)": ["miralia", "golem-ai"],
    "Sekoia.io": ["sekoia", "sekoia-io"],
    "Groupe JVS": ["jvs", "jvs-mairistem"],
    "Berger-Levrault": ["bergerlevrault", "berger-levrault"],
    "Softway Medical": ["softwaymedical", "softway-medical"],
    "Tilak Healthcare": ["tilak", "tilakhealthcare"],
    "Withings Health Solutions": ["withings"],
    "Incepto Medical": ["incepto", "inceptomedical"],
    "Synapse Medicine": ["synapsemedicine", "synapse-medicine"],
    "Nouveal e-santé": ["nouveal"],
    "Mistral AI": ["mistralai", "mistral-ai"],
    "Comand AI": ["comand-ai", "comandai"],
    "Harmattan AI": ["harmattan-ai", "harmattanai"],
    "Craft AI": ["craft-ai", "craftai"],
    "Ciril Group": ["cirilgroup", "ciril"],
    "Clever Cloud": ["clevercloud", "clever-cloud"],
    "Hugging Face": ["huggingface"],
    "Make.org": ["makeorg", "make-org"],
    "Cap Collectif": ["capcollectif", "cap-collectif"],
}


def sans_accent(texte):
    return "".join(c for c in unicodedata.normalize("NFD", texte)
                   if unicodedata.category(c) != "Mn")


def slugs(entreprise):
    """Variantes de slug plausibles pour une entreprise."""
    if entreprise in SLUGS_CONNUS:
        return SLUGS_CONNUS[entreprise]
    base = sans_accent(entreprise.lower())
    base = re.sub(r"\(.*?\)", " ", base)
    base = re.sub(r"\b(sas|sa|group|groupe|medical|ex)\b", " ", base)
    base = re.sub(r"[^a-z0-9]+", " ", base).strip()
    mots = base.split()
    if not mots:
        return []
    candidats = ["".join(mots), "-".join(mots), mots[0], "".join(mots).capitalize()]
    vus, sortie = set(), []
    for c in candidats:
        if c and c not in vus and len(c) > 2:
            vus.add(c)
            sortie.append(c)
    return sortie[:4]


def telecharger(url, cache=True):
    chemin = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9]+", "_", url)[:150] + ".json")
    if cache and os.path.exists(chemin):
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    requete = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(requete, timeout=DELAI) as reponse:
            if reponse.status != 200:
                return None
            donnees = json.loads(reponse.read().decode("utf-8", "replace"))
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError, OSError):
        return None
    os.makedirs(CACHE, exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f)
    return donnees


def normaliser(source, donnees):
    """Ramène les formats des différents ATS à une liste d'offres comparables."""
    offres = []
    if not donnees:
        return offres
    try:
        if source == "ashby":
            brutes = donnees.get("jobs", [])
            for o in brutes:
                offres.append(dict(titre=o.get("title", ""), lieu=o.get("location", ""),
                                   url=o.get("jobUrl", ""), publiee=o.get("publishedAt", ""),
                                   texte=o.get("descriptionPlain", "") or ""))
        elif source == "greenhouse":
            for o in donnees.get("jobs", []):
                offres.append(dict(titre=o.get("title", ""),
                                   lieu=(o.get("location") or {}).get("name", ""),
                                   url=o.get("absolute_url", ""), publiee=o.get("updated_at", ""),
                                   texte=re.sub(r"<[^>]+>", " ", o.get("content", "") or "")))
        elif source == "lever":
            for o in donnees:
                offres.append(dict(titre=o.get("text", ""),
                                   lieu=(o.get("categories") or {}).get("location", ""),
                                   url=o.get("hostedUrl", ""),
                                   publiee=o.get("createdAt", ""),
                                   texte=o.get("descriptionPlain", "") or ""))
        elif source == "recruitee":
            for o in donnees.get("offers", []):
                offres.append(dict(titre=o.get("title", ""), lieu=o.get("location", ""),
                                   url=o.get("careers_url", ""), publiee=o.get("published_at", ""),
                                   texte=re.sub(r"<[^>]+>", " ", o.get("description", "") or "")))
        elif source == "smartrecruiters":
            for o in donnees.get("content", []):
                lieu = o.get("location") or {}
                offres.append(dict(titre=o.get("name", ""), lieu=lieu.get("city", ""),
                                   url=o.get("ref", ""), publiee=o.get("releasedDate", ""), texte=""))
        elif source == "teamtailor":
            for o in donnees.get("jobs", []):
                offres.append(dict(titre=o.get("title", ""), lieu=o.get("location", ""),
                                   url=o.get("careersite-job-url", ""), publiee=o.get("created-at", ""),
                                   texte=re.sub(r"<[^>]+>", " ", o.get("body", "") or "")))
        elif source == "workable":
            for o in donnees.get("jobs", []):
                offres.append(dict(titre=o.get("title", ""), lieu=o.get("location", ""),
                                   url=o.get("url", ""), publiee=o.get("published_on", ""),
                                   texte=re.sub(r"<[^>]+>", " ", o.get("description", "") or "")))
        elif source == "personio":
            for o in (donnees if isinstance(donnees, list) else donnees.get("jobs", [])):
                offres.append(dict(titre=o.get("name", "") or o.get("title", ""),
                                   lieu=o.get("office", ""), url=o.get("url", ""),
                                   publiee=o.get("createdAt", ""),
                                   texte=re.sub(r"<[^>]+>", " ", str(o.get("jobDescriptions", "")))))
        elif source == "join":
            for o in (donnees.get("data", donnees) if isinstance(donnees, dict) else donnees):
                if isinstance(o, dict):
                    offres.append(dict(titre=o.get("title", ""), lieu=o.get("location", ""),
                                       url=o.get("url", ""), publiee=o.get("publishedAt", ""),
                                       texte=re.sub(r"<[^>]+>", " ", o.get("description", "") or "")))
    except (AttributeError, TypeError):
        return []
    return [o for o in offres if o["titre"]]


def chercher_entreprise(entreprise, cache):
    for slug in slugs(entreprise):
        for source, gabarit in ATS.items():
            donnees = telecharger(gabarit.format(slug=slug), cache)
            offres = normaliser(source, donnees)
            if offres:
                for o in offres:
                    o["entreprise"] = entreprise
                    o["source"] = f"{source}:{slug}"
                return offres
    return []


def charger_cibles():
    spec = importlib.util.spec_from_file_location("cibles", os.path.join(ICI, "data", "cibles.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return [dict(zip(mod.CHAMPS, c)) for c in mod.CIBLES]


def main():
    parseur = argparse.ArgumentParser()
    parseur.add_argument("--cache", action="store_true", help="réutiliser les réponses en cache")
    parseur.add_argument("--fils", type=int, default=8)
    args = parseur.parse_args()

    cibles = charger_cibles()
    resultats = []
    with futures.ThreadPoolExecutor(max_workers=args.fils) as pool:
        taches = {pool.submit(chercher_entreprise, c["entreprise"], args.cache): c for c in cibles}
        for tache in futures.as_completed(taches):
            cible = taches[tache]
            for offre in tache.result():
                offre["famille"] = cible["famille"]
                offre["score_cible"] = sum(cible["notes"])
                resultats.append(offre)

    sortie = os.path.join(ICI, "out", "offres.json")
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(dict(genere_le=datetime.now(timezone.utc).isoformat(), offres=resultats), f,
                  ensure_ascii=False)
    entreprises = {o["entreprise"] for o in resultats}
    print(f"{len(resultats)} offres trouvées chez {len(entreprises)} entreprises "
          f"sur {len(cibles)} cibles interrogées")
    print(sortie)


if __name__ == "__main__":
    main()
