# -*- coding: utf-8 -*-
"""Note les offres collectées et produit le classement des opportunités.

Grille sur 18, six critères de 0 à 3, même logique que la notation des cibles :
  intitule   adéquation du titre au poste visé
  seniorite  niveau de responsabilité
  mission    densité de contenu « sphère publique » dans la fiche de poste
  ancrage    poste basé en France
  entreprise priorité de l'entreprise dans la liste de cibles
  fraicheur  date de publication

Usage : python score_offres.py [--seuil 9]
Sortie : out/opportunites.md et out/opportunites.json
"""

import argparse
import json
import os
import re
from datetime import datetime, timezone

ICI = os.path.dirname(os.path.abspath(__file__))

TITRE_FORT = ["affaires publiques", "public affairs", "relations institutionnelles",
              "public policy", "politiques publiques", "partenariats publics", "public sector",
              "secteur public", "government relations", "government affairs", "institutional relations",
              "affaires institutionnelles", "public affairs"]
TITRE_MOYEN = ["market access", "accès au marché", "partenariats institutionnels", "policy",
               "regulatory", "réglementaire", "paritarisme", "union relations", "advocacy",
               "plaidoyer", "relations extérieures", "external relations"]
TITRE_FAIBLE = ["partnership", "partenariat", "alliance", "business strategist", "legal counsel",
                "compliance", "stratégie", "strategy"]

DIRECTION = ["director", "directeur", "directrice", "head of", "vp ", "vice president",
             "chief", "lead ", "responsable", "senior manager"]
INTERMEDIAIRE = ["manager", "senior", "consultant", "chargé", "chargée", "officer", "counsel"]
JUNIOR = ["stage", "stagiaire", "intern", "alternance", "apprenti", "junior", "graduate", "trainee"]

PUBLIC = ["affaires publiques", "public affairs", "relations institutionnelles", "public sector",
          "secteur public", "public policy", "politiques publiques", "pouvoirs publics",
          "ministèr", "gouvernement", "government", "régulateur", "regulator", "hôpital public",
          "collectivité", "marchés publics", "public procurement", "assurance maladie",
          "haute autorité de santé", " has ", "cnam", "ars ", "préfect", "parlement",
          "commission européenne", "european commission", "institutionnel", "lobbying",
          "remboursement", "reimbursement", "agence nationale", "commande publique",
          "entités publiques", "décideurs publics", "appel d'offres", "appels d'offres",
          "administration", "opérateurs publics", "acteurs publics", "établissement public"]

FRANCE = ["france", "paris", "lyon", "marseille", "bordeaux", "nantes", "lille", "toulouse",
          "rennes", "montpellier", "annecy", "biarritz", "grenoble", "strasbourg", "remote"]
HORS_FRANCE = ["united states", "usa", "new york", "san francisco", "palo alto", "boston", "austin",
               "london", "berlin", "munich", "madrid", "milan", "stockholm", "dubai", "dubaï",
               "yerevan", "armenia", "singapore", "tokyo", "amsterdam", "bruxelles", "brussels"]


def note_intitule(titre):
    t = titre.lower()
    if any(m in t for m in TITRE_FORT):
        return 3
    if any(m in t for m in TITRE_MOYEN):
        return 2
    if any(m in t for m in TITRE_FAIBLE):
        return 1
    return 0


def note_seniorite(titre):
    t = " " + titre.lower() + " "
    if any(m in t for m in JUNIOR):
        return 0
    if any(m in t for m in DIRECTION):
        return 3
    if any(m in t for m in INTERMEDIAIRE):
        return 2
    return 1


def note_mission(texte, titre):
    t = (titre + " " + (texte or "")).lower()
    occurrences = sum(t.count(m) for m in PUBLIC)
    if occurrences >= 10:
        return 3
    if occurrences >= 5:
        return 2
    if occurrences >= 2:
        return 1
    return 0


def note_ancrage(lieu):
    l = (lieu or "").lower()
    if not l:
        return 1
    en_france = any(m in l for m in FRANCE)
    hors = any(m in l for m in HORS_FRANCE)
    if en_france and not hors:
        return 3
    if en_france and hors:
        return 2
    if hors:
        return 0
    return 1


def note_entreprise(score_cible):
    if score_cible >= 13:
        return 3
    if score_cible >= 9:
        return 2
    return 1


def age_jours(publiee):
    """Âge de l'offre en jours, quel que soit le format de date de l'ATS."""
    if not publiee:
        return None
    texte = str(publiee).strip()
    if re.fullmatch(r"\d{10,13}", texte):
        horodatage = int(texte) / (1000 if len(texte) > 10 else 1)
        date = datetime.fromtimestamp(horodatage, timezone.utc)
    else:
        try:
            date = datetime.fromisoformat(texte.replace("Z", "+00:00"))
        except ValueError:
            return None
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - date).days


def note_fraicheur(jours):
    if jours is None:
        return 1
    if jours <= 30:
        return 3
    if jours <= 90:
        return 2
    if jours <= 180:
        return 1
    return 0


def noter(offre):
    jours = age_jours(offre.get("publiee"))
    notes = dict(
        intitule=note_intitule(offre["titre"]),
        seniorite=note_seniorite(offre["titre"]),
        mission=note_mission(offre.get("texte"), offre["titre"]),
        ancrage=note_ancrage(offre.get("lieu")),
        entreprise=note_entreprise(offre.get("score_cible", 0)),
        fraicheur=note_fraicheur(jours),
    )
    offre["notes"] = notes
    offre["total"] = sum(notes.values())
    offre["age_jours"] = jours
    return offre


def main():
    parseur = argparse.ArgumentParser()
    parseur.add_argument("--seuil", type=int, default=9)
    parseur.add_argument("--top", type=int, default=10)
    args = parseur.parse_args()

    with open(os.path.join(ICI, "out", "offres.json"), encoding="utf-8") as f:
        brut = json.load(f)
    toutes = list(brut["offres"])
    for o in toutes:
        o.setdefault("statut", "ouverte")   # une offre servie par un ATS est ouverte par construction
        o.setdefault("source_type", "ats")

    # offres repérées hors ATS : on écarte celles dont la clôture est vérifiée
    externes = os.path.join(ICI, "data", "offres_externes.json")
    if os.path.exists(externes):
        with open(externes, encoding="utf-8") as f:
            for o in json.load(f)["offres"]:
                if o.get("statut") != "fermee":
                    o["source_type"] = "web"
                    toutes.append(o)
    offres = [noter(o) for o in toutes]
    # une offre sans aucun signal public n'est pas une opportunité, quel que soit son total
    # L'intitulé prime : une offre dont le titre ne porte pas une mission
    # d'affaires publiques, de secteur public ou d'accès au marché n'est pas
    # une opportunité pour Mehdi, même si sa fiche de poste cite l'Assurance
    # maladie ou un régulateur — c'est le cas de tous les postes juridiques
    # d'un assureur, par exemple.
    retenues = [o for o in offres
                if o["notes"]["intitule"] >= 2 and o["notes"]["mission"] >= 1
                and o["total"] >= args.seuil]
    retenues.sort(key=lambda o: (-o["total"], -o["notes"]["intitule"]))

    with open(os.path.join(ICI, "out", "opportunites.json"), "w", encoding="utf-8") as f:
        json.dump([{k: v for k, v in o.items() if k != "texte"} for o in retenues], f,
                  ensure_ascii=False, indent=1)

    lignes = [f"# Opportunités détectées — {datetime.now().strftime('%d/%m/%Y')}", "",
              f"{len(offres)} offres analysées, {len(retenues)} retenues (score ≥ {args.seuil}/18 "
              f"et contenu affaires publiques avéré).", ""]
    for rang, o in enumerate(retenues[:args.top], 1):
        n = o["notes"]
        age = f"{o['age_jours']} j" if o["age_jours"] is not None else "date inconnue"
        lignes += [f"## {rang}. {o['titre']} — {o['entreprise']} ({o['total']}/18)", "",
                   f"- Lieu : {o['lieu'] or 'non précisé'} · publiée il y a {age} · {o['famille']}"
                   + ("" if o.get("statut") == "ouverte"
                      else " · **statut non vérifié**"),
                   f"- Notes : intitulé {n['intitule']}, séniorité {n['seniorite']}, "
                   f"mission publique {n['mission']}, ancrage {n['ancrage']}, "
                   f"entreprise {n['entreprise']}, fraîcheur {n['fraicheur']}",
                   f"- Offre : {o['url']}", ""]
    chemin = os.path.join(ICI, "out", "opportunites.md")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    print(f"{len(offres)} offres analysées — {len(retenues)} retenues")
    print(chemin)


if __name__ == "__main__":
    main()
