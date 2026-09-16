# Méthodologie

Reprise à l'identique de la grille du fichier initial, pour que les 19 cibles de
la v1 gardent exactement leurs notes et leur priorité.

## Familles

| Famille | Ce qu'on y met | Pitch de Mehdi |
|---|---|---|
| **Santé** | Healthtech, e-santé, medtech logicielle exposées à l'hôpital public, à l'Assurance maladie et aux ARS | Je sais généraliser une solution sur le territoire et sécuriser son financement |
| **Transformation** | GovTech, logiciels des collectivités et de l'État, civic tech, souveraineté numérique | Je sais comment l'administration achète, décide et conduit le changement |
| **IA** | IA souveraine, conformité IA, cybersécurité, défense, vidéo algorithmique | J'ai écrit la stratégie IA de l'État, je sais ce qu'attendent les acheteurs publics |

## Les six critères, notés de 0 à 3

| Critère | 0 | 3 |
|---|---|---|
| **Dépendance publique** | Marché purement privé | Chiffre d'affaires majoritairement public ou entièrement conditionné par une décision publique |
| **IA / numérique** | Pas de composante IA | L'IA est le cœur du produit |
| **Santé** | Hors santé | Santé exclusivement |
| **Déploiement territorial** | Produit centralisé | L'enjeu est le maillage du territoire (préfectures, ARS, collectivités, GHT) |
| **Stade et levée** | Structure fragile | Levée importante et récente, moyens de recruter un profil senior |
| **Poste à créer** | Direction des affaires publiques déjà en place | Aucune fonction affaires publiques, poste entièrement à construire |

**Total sur 18. Priorité : haute si ≥ 13, moyenne si ≥ 9, basse en dessous.**
Les seuils sont modifiables dans le classeur (cellules B16 et B17 de l'onglet
Synthèse) et les notes se recalculent automatiquement.

## Calibrage

Les ancres de la v1 fixent l'échelle et ne doivent pas bouger :

- un **3 en « stade et levée »** suppose une levée importante et récente
  (Parallel, Sêmeia, Naaia) — pas une entreprise simplement rentable ;
- un **3 en « poste à créer »** suppose une structure d'environ soixante
  personnes ou moins, sans fonction affaires publiques identifiée
  (Cap Collectif, Neocity, Giskard, Naaia) ;
- un **1 en « poste à créer »** signale au contraire une équipe déjà
  structurée (Mistral AI, Pennylane, Nabla).

La première version de la liste étendue ressortait à 76 % de priorités hautes,
contre 42 % dans la v1 : les notes des ajouts ont été resserrées
(`CALIBRAGE` dans `data/cibles.py`) pour retrouver cette proportion.
Un contrôle automatique vérifie que le calibrage ne touche jamais une cible v1.

## Résultat

| Famille | Cibles | Priorité haute | Score moyen |
|---|---|---|---|
| Santé | 48 | 34 | 13,6 |
| Transformation | 29 | 5 | 11,3 |
| IA | 27 | 6 | 11,8 |
| **Total** | **104** | **45** | **12,7** |

La famille Santé concentre mécaniquement les priorités hautes : une entreprise
de santé part avec 6 points sur 18 (dépendance publique et santé au maximum).
C'est cohérent avec la v1, où 7 des 8 cibles santé étaient en priorité haute.

## Limites assumées

- Les notes sont une appréciation à partir d'informations publiques, à ajuster
  après les premiers échanges.
- Les signaux d'actualité sont datés de septembre 2026 ; ceux qui n'ont pas pu
  être confirmés sont signalés dans la colonne *Points à vérifier*.
- 15 dirigeants restent à identifier : ils sont listés en fin de
  `out/a_contacter.md`.

---

# Notation des offres (routine 2)

Même forme que la notation des cibles : six critères de 0 à 3, total sur 18.

| Critère | 0 | 3 |
|---|---|---|
| **Intitulé** | Sans rapport | Affaires publiques, relations institutionnelles, secteur public, partenariats publics |
| **Séniorité** | Stage, alternance, junior | Directeur, head of, chief, VP |
| **Mission publique** | Aucune mention de la sphère publique | La fiche de poste est saturée d'enjeux publics (ministères, régulateurs, collectivités, remboursement) |
| **Ancrage** | Poste hors de France | Poste en France, sans rattachement étranger |
| **Entreprise** | Hors liste de cibles | Cible en priorité haute |
| **Fraîcheur** | Publiée il y a plus de six mois | Publiée il y a moins d'un mois |

**Filtre appliqué avant le classement** : une offre n'est retenue que si son
**intitulé** vaut au moins 2 et sa **mission publique** au moins 1. Sans ce
filtre, tous les postes juridiques d'un assureur santé remontent en tête : leurs
fiches citent l'Assurance maladie et les régulateurs à chaque paragraphe sans
qu'il s'agisse pour autant de postes d'affaires publiques.

## Ce que le premier relevé apprend (16/09/2026)

- **704 offres analysées, 8 retenues.** Chez les 104 cibles, une seule offre
  porte explicitement les affaires publiques dans son intitulé (Doctolib).
- **La couverture ATS est de 18 entreprises sur 104.** Les autres utilisent un
  outil sans API publique ou une page carrière maison. Elle progresse en
  complétant `SLUGS_CONNUS` dans `scan_offres.py`.
- **Trois offres vérifiées sur quatre étaient déjà fermées** côté sites
  d'emploi. Les pages restent indexées bien après la clôture : toute offre
  trouvée par moteur de recherche doit être vérifiée page à page.
- **Ce constat valide la routine 1** : dans cet écosystème, le poste que vise
  Mehdi est plus souvent à créer qu'à pourvoir.
