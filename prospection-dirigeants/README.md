# Routine de prospection — dirigeants cibles pour Mehdi Kellal

Objectif : identifier en continu les dirigeants à contacter dans les entreprises
où un poste d'**affaires publiques, de partenariats publics ou de Head of Public
Sector** a du sens pour Mehdi Kellal, suivre leur actualité, et produire le
message LinkedIn correspondant.

Cette routine prolonge le fichier `Cibles_Mehdi_Kellal_Sante_Transfo_IA.xlsx`
(19 cibles) en appliquant la même méthodologie à **104 entreprises**.

## Contenu

| Fichier | Rôle |
|---|---|
| `data/cibles.py` | La base : 104 entreprises, notes, signaux d'actualité, sources, dirigeants |
| `METHODOLOGIE.md` | La grille de notation et les règles de calibrage |
| `build_workbook.py` | Génère le classeur Excel et le fichier de messages |
| `messages.py` | Génère la note de connexion (300 caractères) et le premier message |
| `selection.py` | Sort les 10 prochains dirigeants à contacter |
| `ROUTINE_PROMPT.md` | Prompt de la routine 1 — veille des dirigeants |
| `scan_offres.py` | Balaie les ATS des 104 cibles et collecte les offres ouvertes |
| `score_offres.py` | Note les offres et sort le classement des opportunités |
| `data/offres_externes.json` | Offres repérées hors ATS, avec leur statut de vérification |
| `ROUTINE_OFFRES_PROMPT.md` | Prompt de la routine 2 — veille des offres d'emploi |

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

**Routine 1 — dirigeants à approcher**

```bash
python build_workbook.py          # -> out/Cibles_Mehdi_Kellal_v2.xlsx + out/messages_linkedin.md
python selection.py               # -> out/a_contacter.md (10 dirigeants prioritaires)
python selection.py out/Cibles_Mehdi_Kellal_v2.xlsx 20   # 20 au lieu de 10
```

**Routine 2 — offres d'emploi ouvertes**

```bash
python scan_offres.py             # -> out/offres.json (balayage des ATS des 104 cibles)
python scan_offres.py --cache     # réutilise le relevé précédent
python score_offres.py --top 10   # -> out/opportunites.md
```

Le dossier `out/` n'est pas versionné : il est régénéré à chaque exécution.

## Suivi des contacts

L'onglet **Contacts** du classeur comporte trois colonnes de suivi à remplir à
la main : *Date de contact*, *Réponse*, *Suite à donner*. `selection.py` écarte
automatiquement les lignes dont la date de contact est renseignée : il suffit de
conserver le même classeur d'une semaine sur l'autre, ou de recopier ces trois
colonnes après une régénération.

## Les sources d'offres, et leurs limites

| Source | Accès | Fiabilité |
|---|---|---|
| **API publiques des ATS** (Ashby, Greenhouse, Lever, Recruitee, SmartRecruiters, Teamtailor, Workable, Personio, Join) | Ouvert, structuré, daté | **Élevée** : un ATS ne sert que des offres ouvertes |
| **Welcome to the Jungle** | Recherche de postes et listes d'offres derrière authentification ; pages d'offres individuelles indexées | Moyenne : la page survit à la clôture du poste, vérification obligatoire |
| **LinkedIn Jobs, Indeed** | Authentification et anti-robot ; extraction automatisée interdite par leurs conditions | Faible : utilisables seulement via le moteur de recherche, vérification obligatoire |
| **Pages carrières maison** | Variables | Moyenne : à traiter au cas par cas, en repérant l'ATS sous-jacent |

Au premier relevé, la couverture ATS est de **18 entreprises sur 104**, et
**3 des 4 offres vérifiées côté sites d'emploi étaient déjà fermées**.

## Ce que la routine ne fait pas

- Elle **n'envoie aucun message** et **ne postule à rien**. Messages et
  candidatures restent manuels.
- Elle **n'enrichit ni email ni téléphone** : décision de Jenny, les dirigeants
  sont identifiés par recherche seule, sans consommation de crédits FullEnrich.
- Elle **ne contourne aucune protection** : pas de compte automatisé ni de
  contournement d'anti-robot sur les sites d'emploi.
- Elle **ne garantit pas** que les postes visés sont ouverts : la colonne
  *Points à vérifier* signale, pour chaque cible, ce qu'il faut confirmer avant
  d'approcher (dernière levée, existence d'une équipe affaires publiques,
  dirigeant en poste).
