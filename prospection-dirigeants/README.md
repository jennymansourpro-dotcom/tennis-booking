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
| `ROUTINE_PROMPT.md` | Le prompt exact de la routine planifiée |

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python build_workbook.py          # -> out/Cibles_Mehdi_Kellal_v2.xlsx + out/messages_linkedin.md
python selection.py               # -> out/a_contacter.md (10 dirigeants prioritaires)
python selection.py out/Cibles_Mehdi_Kellal_v2.xlsx 20   # 20 au lieu de 10
```

Le dossier `out/` n'est pas versionné : il est régénéré à chaque exécution.

## Suivi des contacts

L'onglet **Contacts** du classeur comporte trois colonnes de suivi à remplir à
la main : *Date de contact*, *Réponse*, *Suite à donner*. `selection.py` écarte
automatiquement les lignes dont la date de contact est renseignée : il suffit de
conserver le même classeur d'une semaine sur l'autre, ou de recopier ces trois
colonnes après une régénération.

## Ce que la routine ne fait pas

- Elle **n'envoie aucun message**. Les messages sont des bases à relire et à
  adapter ; l'envoi reste manuel, sur LinkedIn.
- Elle **n'enrichit ni email ni téléphone**. Les dirigeants sont identifiés par
  recherche (FullEnrich + presse), sans consommation de crédits d'enrichissement.
  Un enrichissement est possible mais doit être décidé explicitement.
- Elle **ne garantit pas** que les postes visés sont ouverts : la colonne
  *Points à vérifier* signale, pour chaque cible, ce qu'il faut confirmer avant
  d'approcher (dernière levée, existence d'une équipe affaires publiques,
  dirigeant en poste).
