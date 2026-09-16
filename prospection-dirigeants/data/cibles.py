# -*- coding: utf-8 -*-
"""Liste de cibles pour la recherche de poste de Mehdi Kellal.

Colonnes des notes (0-3) : dep = dependance a la decision publique,
ia = intensite IA/numerique, sante = exposition sante, terr = enjeu de
deploiement territorial, stade = capacite a financer le poste (levee/taille),
poste = probabilite qu'un poste affaires publiques soit a creer.

origine : v1 = liste initiale fournie par Jenny, v2 = ajout de septembre 2026.
"""

CHAMPS = ("famille", "entreprise", "quoi", "notes", "signal", "source",
          "angle", "verif", "origine", "nom", "fonction", "linkedin",
          "accroche", "statut")

CIBLES = [
# ---------------------------------------------------------------- SANTE (v1)
("Santé", "Parallel", "Agents IA pour l'administratif hospitalier (codage PMSI)", (3,3,3,2,3,3),
 "Série A de 20 M$ (2026), 30 recrutements prévus d'ici fin 2026",
 "https://www.planet-tech.fr/parallel-leve-20m-agents-ia-revolutionnent-hopital/",
 "Hôpital public, financement T2A, IA agentique", "Univers proche de Granit (back-office santé), à garder en tête", "v1",
 "Paul Lafforgue", "Cofondateur et CEO", "", "Ancien data scientist chez Meta ; cofondateur passé par la création d'Hublo", "Identifié via presse"),

("Santé", "Sêmeia", "Télésurveillance multipathologie avec IA", (3,2,3,3,3,2),
 "Levée de 21 M€ (mai 2026), 35 000 patients, 500 établissements, Banque des Territoires au capital",
 "https://application-sante-numerique.fr/blog/healthtech-francaise-levees-fonds-158-millions-q1-2026/",
 "Généralisation territoriale, parcours de soins", "CEO actuel à confirmer", "v1",
 "Marlène Hayaux du Tilly", "COO", "https://www.linkedin.com/in/marlenehayauxdutilly", "Ancienne secrétaire générale dans le secteur associatif", "Identifié"),

("Santé", "Tessan", "Téléconsultation en pharmacies et mairies", (3,1,3,3,2,2),
 "Plus de 500 structures équipées, dont des collectivités ; 165 salariés",
 "", "Déserts médicaux, collectivités, préfets", "CEO à confirmer (données FullEnrich incohérentes sur les cofondateurs)", "v1",
 "Antoine Ducrocq", "Chief Marketing Officer", "https://www.linkedin.com/in/aducrocq", "Ex-Qonto, Criteo, Teads", "Identifié"),

("Santé", "Therapixel", "IA en mammographie", (3,3,3,2,1,2),
 "Acteur de référence de l'IA en dépistage organisé du cancer du sein",
 "", "Dépistage organisé, politique de santé publique", "Présence forte aux États-Unis", "v1",
 "Matthieu Leclerc-Chalvet", "CEO", "https://www.linkedin.com/in/matthieulc", "Thèse sur l'adoption des innovations médicales", "Identifié"),

("Santé", "AZmed", "IA de détection des fractures", (2,3,3,2,2,2),
 "Déployée dans plus de 2 500 établissements",
 "https://www.planetegrandesecoles.com/ia-sante-2026-startup",
 "Passage à l'échelle nationale, régulation IA", "Dernière levée à vérifier", "v1",
 "Julien Vidal", "Cofondateur et CEO", "https://www.linkedin.com/in/julien-vidal-b37071b7", "Forbes 30 under 30", "Identifié"),

("Santé", "Rofim", "Téléexpertise et e-RCP", (3,1,3,3,2,2),
 "CEO lauréate Choiseul Next Gen Leaders 2026 (top 40 santé) ; déploiements GHT et ARS ; 57 salariés",
 "", "Parcours territoriaux, financement de la téléexpertise, feuille de route télémédecine 2026-2028",
 "Contact CEO désormais identifié (était à compléter dans la v1)", "v1",
 "Emilie Mercadal", "Cofondatrice et CEO", "https://www.linkedin.com/in/emilie-mercadal-rofim", "Lauréate Choiseul Next Gen Leaders 2026 ; basée à Marseille", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Calmedica", "Suivi patient automatisé par IA conversationnelle", (3,3,3,1,1,2),
 "Plus de 15 millions de patients suivis dans une centaine de services hospitaliers",
 "", "Hôpitaux publics, AI Act", "Structure de 25 personnes, capacité à financer le poste", "v1",
 "Alexis Hernot", "Cofondateur et directeur général", "https://www.linkedin.com/in/alexis-hernot", "Polytechnicien, président du groupe X Santé Biotech, partner chez 50 Partners", "Identifié"),

("Santé", "Nabla", "Assistant IA pour médecins", (2,3,3,1,2,1),
 "Série C de 61 M€ ; nouveau CEO basé aux États-Unis depuis juillet 2026",
 "", "Hôpital public français, AI Act", "Recentrage américain probable : vérifier le besoin France", "v1",
 "Brian Manning", "CEO (depuis juillet 2026)", "https://www.linkedin.com/in/briancmanning", "Basé à Boston : vérifier qui porte la France", "Identifié"),

# ---------------------------------------------------------------- SANTE (v2)
("Santé", "Doctolib", "Prise de rendez-vous, logiciels médicaux et IA de santé", (2,3,3,3,1,1),
 "Création d'un laboratoire de recherche en santé (juillet 2026) avec Inria, Inserm et Université Paris-Cité ; polémique sur l'entraînement d'IA à partir des données de santé (juin-juillet 2026) ; rachat de Medicus Health au Royaume-Uni (mai 2026)",
 "https://dsih.fr/articles/6203/", "Confiance dans les données de santé, cadre CNIL MR004, acceptabilité politique de l'IA en santé",
 "Équipe affaires publiques déjà structurée : viser un poste adjoint ou un mandat 'IA et confiance'", "v2",
 "Nacim Rahal", "Directeur IA et Data", "", "Pilote le laboratoire de recherche IA annoncé en juillet 2026", "Identifié via presse"),

("Santé", "Lifen", "Plateforme de coordination et d'échange de documents médicaux", (3,2,3,3,2,3),
 "175 à 195 salariés ; 70 M€ levés au total ; positionnement Ségur du numérique en santé",
 "https://fr.wikipedia.org/wiki/Lifen", "Ségur numérique, financement des établissements, interopérabilité",
 "Philippe Douste-Blazy est cofondateur : réseau institutionnel déjà dense, vérifier le besoin réel", "v2",
 "Franck Le Ouay", "Cofondateur et CEO", "https://www.linkedin.com/in/franckl", "Cofondateur et ancien directeur scientifique de Criteo", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Arkhn", "Entrepôts de données de santé (EDS) pour les hôpitaux", (3,3,3,3,2,3),
 "Équipe plus d'un tiers des CHU français ; lancement d'Arkhn Assistant, outils IA souverains ; projet Darah avec Roche et Bpifrance publié en 2025",
 "https://www.roche.fr/media/roche-arkhn-analyse-sante", "Souveraineté des données de santé, EDS, recherche publique, France 2030",
 "Structure de 25 personnes : vérifier la capacité à financer un poste senior", "v2",
 "Théo Ryffel", "Cofondateur", "https://www.linkedin.com/in/theoryffel", "Docteur, cofondateur ; réseau OpenMined et recherche publique", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Galeon", "Dossier patient informatisé nativement IA, partagé entre établissements", (3,3,3,3,2,3),
 "Campagne de financement participatif en obligations (janvier-février 2026) puis en titres de capital jusqu'au 23 juin 2026 ; 19 hôpitaux publics dont 2 CHU, plus de 10 000 soignants",
 "https://www.galeon.care/fr/blog/levee-de-fonds-galeon-2026", "Dossier national de santé, pilotage régional, facturation PMSI/CCAM automatisée",
 "Financement participatif plutôt que VC : vérifier la trésorerie disponible pour un recrutement senior", "v2",
 "Loïc Brotons", "Cofondateur et CEO (médecin)", "https://www.linkedin.com/in/loki1", "Médecin innovateur, basé à Annecy", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Sancare", "IA de codage et de valorisation de l'activité hospitalière (PMSI)", (3,3,3,2,1,3),
 "Discussions exclusives avec Dedalus France annoncées en janvier 2025 pour un partenariat stratégique sur le codage",
 "https://www.hospitalia.fr/tags/Sancare/", "T2A, recettes des hôpitaux publics, IA documentaire",
 "Vérifier l'issue du rapprochement avec Dedalus avant d'approcher", "v2",
 "Marc Michel", "Chief Scientific Officer", "https://www.linkedin.com/in/marc-michel-26499273", "Porte la crédibilité scientifique du codage IA", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Implicity", "Télésurveillance cardiaque et analyse IA des données de dispositifs implantés", (3,3,3,2,3,3),
 "40 M$ levés le 9 septembre 2026 (IRIS, Five Arrows) ; inscription au remboursement de la télésurveillance par arrêté (juillet 2026, avis CNEDiMTS de février 2026) ; 250 centres, 120 000 patients",
 "https://www.globenewswire.com/news-release/2026/09/09/3358622/0/en/implicity-secures-40m-growth-equity-funding-to-scale-its-ai-driven-cardiac-monitoring-platform-globally.html",
 "Remboursement de la télésurveillance, CNEDiMTS, LFSS : cœur de métier affaires publiques",
 "CEO basé à Cambridge (États-Unis) : identifier qui porte la France", "v2",
 "Arnaud Rosier", "Cofondateur et CEO (cardiologue)", "https://www.linkedin.com/in/arnaud-rosier-94b05410", "Rythmologue, docteur en IA ; partage son temps entre Paris et Boston", "Identifié via presse"),

("Santé", "Omnidoc", "Plateforme de téléexpertise, e-RCP et téléconsultation assistée", (3,2,3,3,2,3),
 "122 000 utilisateurs, 2,5 millions de téléexpertises, 92 spécialités (bilan publié début 2026) ; rémunération de la téléexpertise portée à 23 € au 1er janvier 2026 ; ouverture de la Belgique",
 "https://omnidoc.fr/actualites/", "Financement conventionnel de la téléexpertise, lien ville-hôpital, maisons France Santé",
 "58 salariés : vérifier la capacité à financer un poste de direction", "v2",
 "Baptiste Truchot", "Cofondateur et président", "", "S'exprime publiquement sur le cadre réglementaire de l'adressage et de la téléexpertise", "Identifié via presse"),

("Santé", "Incepto Medical", "Plateforme de distribution d'applications d'IA en imagerie", (3,3,3,3,2,3),
 "Présent dans une vingtaine de CH et CHU de premier plan (AP-HP, Grenoble, Montpellier, Nancy, Poitiers, Rennes) et dans cinq pays européens",
 "https://www.lbofrance.com/incepto-specialiste-de-la-sante-digitale-leve-27-millions-deuros/",
 "Financement de l'IA en imagerie, forfait innovation, marchés publics hospitaliers", "Dernière levée et actualité 2026 à vérifier", "v2",
 "Antoine Jomier", "Cofondateur et président", "", "Porte le discours public d'Incepto sur la diffusion de l'IA en imagerie", "Identifié via presse"),

("Santé", "Milvue", "IA de radiologie (urgences, pédiatrie, ostéoarticulaire, thorax)", (2,3,3,3,2,3),
 "Plus de 600 sites déployés dans 25 pays, 40 millions d'analyses par an ; marquages CE, FDA et Santé Canada",
 "https://www.milvue.com", "Urgences, pertinence des actes, déploiement en CHU", "Dernière levée à vérifier ; équipe de 31 personnes", "v2",
 "Alexandre Parpaleix", "Cofondateur, président et directeur médical", "https://www.linkedin.com/in/alexandre-parpaleix", "Radiologue, docteur en neurosciences", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Raidium", "Modèle de fondation d'IA pour la radiologie (modèle Curia)", (3,3,3,2,2,3),
 "Modèle multimodal Curia présenté lors de la journée IA et imagerie du GCS HUGO (Nantes, mai 2026) ; partenariats avec Pompidou, Beaujon, Fondation Rothschild et des centres anticancéreux",
 "https://www.chu-hugo.fr/actualites/intelligence-artificielle-en-imagerie-medicale-des-promesses-aux-usages-concrets/",
 "France 2030, modèles de fondation souverains en santé, évaluation par la HAS", "51 salariés ; ambition américaine affichée", "v2",
 "Paul Hérent", "Cofondateur (radiologue)", "", "Radiologue de formation, cofondateur avec Pierre Manceron", "Identifié via presse"),

("Santé", "TheraPanacea", "IA pour la radiothérapie et la radio-oncologie", (3,3,3,2,2,3),
 "Issue d'Inria et CentraleSupélec, laboratoire commun avec Gustave Roussy",
 "", "Plan cancer, équipement des centres de radiothérapie, achats hospitaliers", "Dernière levée et effectif 2026 à vérifier", "v2",
 "Nikos Paragios", "Fondateur et CEO", "https://www.linkedin.com/in/nikos-paragios-20777869", "Professeur, fondateur issu de la recherche publique", "Identifié via presse"),

("Santé", "Kiro", "IA appliquée à la biologie médicale et à la pertinence des examens", (3,3,3,3,2,3),
 "Projet OPTIMABIO avec l'AP-HM, les Hospices Civils de Lyon et le CHU de Limoges ; budget global supérieur à 17 M€ ; nouvelle levée visée à horizon 2028",
 "https://www.pocmedia.fr/trois-chu-sallient-a-la-startup-kiro-pour-mieux-orienter-les-examens-biologiques-a-lhopital/",
 "Pertinence des actes, dépenses de biologie de l'Assurance maladie, consortium CHU", "Structure marseillaise ; vérifier le calendrier de financement", "v2",
 "Alexandre Guenoun", "Fondateur et président", "", "Porte le projet OPTIMABIO avec trois CHU", "Identifié via presse"),

("Santé", "Synapse Medicine", "Plateforme de bon usage du médicament (Medication Intelligence)", (3,3,3,2,2,3),
 "Collaborations avec CHU de Bordeaux, Rennes, AP-HP et l'INSERM ; 83 salariés",
 "https://buzz-esante.fr/synapse-medicine-plateforme-de-medication-intelligence-dediee-au-bon-usage-du-medicament/",
 "Iatrogénie médicamenteuse (enjeu de santé publique), certification des LAP, pharmacovigilance", "Actualité 2026 et dernière levée à vérifier", "v2",
 "Clément Goehrs", "Cofondateur et CEO (médecin)", "", "Médecin, cofondateur ; travaux avec le CHU de Bordeaux, l'INSERM et Stanford", "Identifié via presse"),

("Santé", "Posos", "Moteur de recherche et d'aide à la prescription médicamenteuse", (3,3,3,2,2,3),
 "60 salariés ; positionnement aide à la décision médicamenteuse et IA",
 "", "Certification des logiciels d'aide à la prescription, bon usage du médicament", "Dernière levée et clients publics à vérifier", "v2",
 "Emmanuel Bilbault", "Cofondateur et CEO", "https://www.linkedin.com/in/bilbault", "Médecin de formation, discours public sur l'IA de prescription", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Resilience", "Télésurveillance et suivi des patients atteints de cancer", (3,2,3,3,3,2),
 "Cofondée avec Gustave Roussy ; déploiement dans les établissements Ramsay Santé ; 40 M€ levés en série A",
 "https://www.resilience.care/fr/ressources/resilience-se-deploie-dans-11-etablissements-du-groupe-ramsay-sante",
 "Remboursement de la télésurveillance en oncologie, stratégie décennale cancer", "Fondateurs très en réseau (Céline Lazorthes, Jonathan Benhamou) : vérifier l'existence d'un poste", "v2",
 "Céline Lazorthes", "Cofondatrice", "", "Fondatrice de Leetchi, figure publique de la tech française", "Identifié via presse"),

("Santé", "Cureety", "Télésurveillance et suivi des patients en oncologie", (3,2,3,3,2,3),
 "95 salariés ; positionnement télésurveillance remboursée",
 "", "Remboursement de la télésurveillance, parcours cancer", "Actualité 2026 et dernière levée à vérifier", "v2",
 "Nicolas Begin", "Directeur général", "https://www.linkedin.com/in/nicolas-begin-60805b36", "Directeur général, basé à Paris", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Tilak Healthcare", "Dispositif médical numérique de suivi des maladies chroniques de l'œil (OdySight)", (3,2,3,2,2,3),
 "Remboursement d'OdySight obtenu via le dispositif PECAN (avis favorable HAS, octobre 2025) ; création d'un comité scientifique ; pitch au Tech Tour Growth Health 2026",
 "https://www.businesswire.com/news/home/20251010975557/en/",
 "PECAN, accès précoce des dispositifs médicaux numériques, passage au droit commun", "59 salariés ; l'enjeu est le passage du PECAN au remboursement de droit commun", "v2",
 "Edouard Gasser", "Cofondateur et CEO", "", "Porte publiquement le sujet du remboursement des DMN", "Identifié via presse"),

("Santé", "Poppins", "Thérapie numérique pour les enfants dyslexiques", (3,2,3,2,2,3),
 "Avis favorable de la HAS le 30 juin 2026 : deuxième application thérapeutique remboursée en France (après Ludocare) ; 65 salariés",
 "https://www.economiematin.fr/dyslexie-poppins-premiere-app-remboursee",
 "PECAN, remboursement des thérapies numériques, retard français face aux 50 dispositifs remboursés en Allemagne",
 "Validation ministérielle du remboursement encore à confirmer : fenêtre idéale pour un poste affaires publiques", "v2",
 "François Vonthron", "Cofondateur et CEO", "https://www.linkedin.com/in/francoisvonthron", "Porte le discours public sur le retard français en matière de remboursement des DMN", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Ludocare", "Thérapie digitale pour l'asthme de l'enfant (JOE)", (3,2,3,2,1,3),
 "Avis favorable de la HAS en avril 2026 : première thérapie digitale française validée en vue d'une prise en charge de droit commun",
 "https://www.economiematin.fr/dyslexie-poppins-premiere-app-remboursee",
 "Droit commun du remboursement des DMN, observance thérapeutique", "Petite structure : vérifier la capacité de financement", "v2",
 "", "CEO", "", "", "À compléter"),

("Santé", "Lucine", "Thérapies numériques de la douleur", (3,2,3,2,1,3),
 "Positionnement thérapies numériques et douleur chronique",
 "", "Prise en charge de la douleur chronique, accès au remboursement", "Situation financière et dirigeant 2026 à vérifier", "v2",
 "", "CEO", "", "", "À compléter"),

("Santé", "Ambler", "Plateforme de commande et d'optimisation du transport sanitaire", (3,2,3,3,2,3),
 "Réforme du financement des transports inter-hospitaliers ; marché de 5 Md€ par an pour l'Assurance maladie",
 "https://buzz-esante.fr/ambler-digitalise-les-transports-sanitaires/",
 "Dépenses de transport sanitaire de l'Assurance maladie, réforme du financement, hôpitaux publics", "Dernière levée et effectif 2026 à vérifier", "v2",
 "Mehdi Ben Abroug", "Cofondateur et CEO", "", "Porte le sujet de la structuration du transport sanitaire", "Identifié via presse"),

("Santé", "Ambuliz", "Régulation des flux de transport sanitaire pour les établissements", (3,2,3,3,1,3),
 "Déployée dans une quarantaine d'hôpitaux, majoritairement dans l'Ouest ; groupe Vivalto au capital",
 "https://www.bretagne-economique.com/actualites/le-rennais-ambuliz-repense-le-transport-sanitaire-et-leve-1-million-deuros-notamment/",
 "Flux hospitaliers, dépenses de transport, ancrage territorial", "Petite structure rennaise : vérifier la capacité à financer un poste", "v2",
 "Antoine Bohuon", "Cofondateur", "", "Porte le discours sur les tours de contrôle des flux hospitaliers", "Identifié via presse"),

("Santé", "Happytal", "Services aux patients et préadmission en ligne à l'hôpital", (3,1,3,3,2,3),
 "Présent dans plus d'une centaine d'établissements (hôpitaux publics, cliniques, EHPAD)",
 "", "Recettes annexes des hôpitaux publics, expérience patient, chambres particulières", "Actionnariat et dirigeant 2026 à vérifier", "v2",
 "", "Direction générale", "", "", "À compléter"),

("Santé", "Medaviz", "Téléconsultation et téléconsultation assistée territoriale", (3,1,3,3,1,3),
 "Agrément Société de téléconsultation délivré par le ministère de la Santé ; déploiements en EHPAD, CPTS et centres pénitentiaires ; 33 salariés",
 "https://www.medaviz.com/teleconsultation-assistee-et-protocole-de-soins-personnalise/",
 "Feuille de route télémédecine 2026-2028, maisons France Santé, publics fragiles", "Petite structure : vérifier la capacité à financer un poste", "v2",
 "Jean Spalaikovitch", "Cofondateur et directeur médical", "https://www.linkedin.com/in/dr-jean-spalaikovitch-76522844", "Médecin généraliste, cofondateur", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Nouveal e-santé", "Parcours patient numérique pour les établissements de santé", (3,2,3,3,1,3),
 "Positionnement parcours patient et lien avec les établissements publics",
 "", "Ségur numérique, parcours patient, financement des établissements", "Actualité 2026, effectif et dirigeant à vérifier", "v2",
 "", "Direction générale", "", "", "À compléter"),

("Santé", "Exolis", "Parcours de soins numériques et engagement patient", (3,2,3,3,1,3),
 "Positionnement parcours patient pour établissements publics et privés",
 "", "Ségur numérique, télésurveillance, parcours patient", "Actualité 2026 et dirigeant à vérifier (homonymie avec le cabinet RH Exolys)", "v2",
 "", "Direction générale", "", "", "À compléter"),

("Santé", "BioSerenity", "Diagnostic neurologique et cardiaque connecté", (3,3,3,3,2,3),
 "271 salariés ; activité de diagnostic à distance en lien avec les établissements",
 "", "Remboursement des actes de diagnostic, accès aux soins dans les territoires", "Situation financière 2026 à vérifier avant approche", "v2",
 "Marc Frouin", "COO", "https://www.linkedin.com/in/marcfrouin", "Directeur des opérations", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Wandercraft", "Exosquelettes de marche auto-stabilisés et robotique", (3,3,3,2,3,3),
 "75 M€ levés avec l'entrée de Renault, Bpifrance et la BEI au capital ; commercialisation de l'exosquelette personnel Eve prévue en 2026 ; plus de 110 M€ levés au total",
 "https://www.lembarque.com/article/ia-et-robotique-le-francais-wandercraft-annonce-une-levee-de-fonds-de-75-millions-deuros-et-lentree-de-renault-dans-son-capital",
 "Remboursement des dispositifs médicaux (LPPR), France 2030, souveraineté industrielle", "185 salariés ; forte dynamique américaine à prendre en compte", "v2",
 "Alexandre Boulanger", "Cofondateur", "https://www.linkedin.com/in/alexandre-boulanger", "Entrepreneur du dispositif médical, également cofondateur de Metyos", "Identifié (FullEnrich, 09/2026)"),

("Santé", "FeetMe", "Semelles connectées et analyse de la marche", (3,3,3,2,1,3),
 "Positionnement dispositif médical numérique avec enjeu de remboursement",
 "", "Inscription à la LPPR, télésurveillance, rééducation", "Situation financière et dirigeant 2026 à vérifier", "v2",
 "", "CEO", "", "", "À compléter"),

("Santé", "Softway Medical", "Dossier patient informatisé Hopital Manager", (3,2,3,3,2,2),
 "Premier DPI référencé Ségur V2 par l'Agence du numérique en santé (novembre 2025) ; collaboration avec Microsoft Dragon Copilot ; 760 salariés",
 "https://www.hospitalia.fr/tags/Manager/", "Ségur du numérique en santé, souveraineté des SIH, marchés publics hospitaliers",
 "ETI structurée : vérifier s'il existe déjà une direction des relations institutionnelles", "v2",
 "Grégory Rougon", "Directeur produit", "https://www.linkedin.com/in/grégory-rougon-97b26a85", "Porte l'offre DPI référencée Ségur V2", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Maincare", "Logiciels pour les établissements de santé publics", (3,2,3,3,1,2),
 "431 salariés ; partenariat historique avec Sancare pour l'IA de codage",
 "", "Ségur numérique, GHT, convergence des SIH", "Actionnariat et gouvernance 2026 à vérifier", "v2",
 "Dalil Zaïdi", "CTO", "https://www.linkedin.com/in/dalil-zaidi", "Directeur technique", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Enovacom", "Interopérabilité et sécurité des données de santé (Orange Business)", (3,2,3,3,1,1),
 "521 salariés ; filiale d'Orange Business",
 "", "Ségur numérique, interopérabilité, HDS", "Filiale d'un grand groupe : les affaires publiques sont probablement portées par Orange", "v2",
 "Laurent Frigara", "Cofondateur et CEO", "https://www.linkedin.com/in/laurentfrigara", "Cofondateur, dirige Enovacom au sein d'Orange Business", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Weda", "Logiciel médical en ligne pour la médecine de ville (groupe Vidal)", (3,2,3,3,1,2),
 "115 salariés ; adossé au groupe Vidal",
 "", "Ségur numérique en ville, Mon espace santé, certification des LAP", "Appartenance à un groupe : vérifier l'autonomie sur les affaires publiques", "v2",
 "Guillaume de Bruc", "Directeur général", "https://www.linkedin.com/in/guillaume-de-bruc-20346512", "Directeur général, également au sein du groupe Vidal", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Medadom", "Bornes et cabines de téléconsultation en pharmacie et en mairie", (3,2,3,3,2,3),
 "221 salariés ; membre du Next40",
 "", "Déserts médicaux, encadrement de la téléconsultation par la LFSS, collectivités", "Cadre réglementaire des cabines en évolution : enjeu affaires publiques direct", "v2",
 "Elie-Dan Mimouni", "Cofondateur et CEO", "https://www.linkedin.com/in/elie-dan-mimouni-21a198124", "Cofondateur, entreprise membre du Next40", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Qare", "Téléconsultation et organisation de l'offre de soins", (3,2,3,3,1,2),
 "Adossé au groupe européen HealthHero",
 "", "Feuille de route télémédecine 2026-2028, accès aux soins", "Gouvernance française à vérifier (groupe britannique)", "v2",
 "", "Direction générale France", "", "", "À compléter"),

("Santé", "Alan", "Assurance santé et services de santé numériques", (3,3,3,3,3,2),
 "785 M€ de revenus récurrents fin 2025, objectif 1 Md€ en 2026 ; contrat de protection sociale complémentaire des agents publics avec 135 000 agents invités en moins de deux semaines (janvier 2026)",
 "https://www.larevuedudigital.com/le-neo-assureur-sante-alan-enregistre-785-millions-deuros-de-revenus-recurrents/",
 "Protection sociale complémentaire des agents publics, réforme du 100 % santé, prévention",
 "Scale-up structurée : vérifier l'existence d'une équipe affaires publiques et le périmètre secteur public", "v2",
 "Jean-Charles Samuelian-Werve", "Cofondateur et CEO", "", "Cofondateur, s'exprime sur le modèle de l'assurance santé et la prévention", "Identifié via presse"),

("Santé", "Owkin", "IA pour la recherche biomédicale et la pathologie numérique", (3,3,3,2,3,2),
 "Lancement d'une infrastructure agentique de biologie annoncée à la conférence JPM Healthcare 2026 ; réseau de plus de 800 hôpitaux ; consortium français PortrAIt",
 "https://agro-mundi.com/owkin-rapproche-la-superintelligence-biologique-de-la-realite-grace-a-une-nouvelle-infrastructure-dia-de-decouvertes-biologiques/",
 "France 2030, recherche publique, partenariats hospitaliers, souveraineté des données", "Entreprise franco-américaine : vérifier le centre de gravité des décisions", "v2",
 "Thomas Clozel", "Cofondateur et CEO (médecin)", "", "Médecin hématologue, cofondateur", "Identifié via presse"),

("Santé", "Bioptimus", "Modèles de fondation d'IA pour la biologie et la santé", (2,3,3,1,3,3),
 "44 salariés ; dirigée par l'ancien responsable de la recherche IA d'Owkin et ancien de Google Brain",
 "", "France 2030, modèles de fondation souverains, accès aux données de santé", "Positionnement recherche : vérifier la maturité commerciale et l'intérêt pour le secteur public", "v2",
 "Jean-Philippe Vert", "Cofondateur et CEO", "https://www.linkedin.com/in/djipay", "Ancien directeur scientifique d'Owkin, ancien de Google Brain, professeur", "Identifié (FullEnrich, 09/2026)"),

("Santé", "Gleamer", "IA de radiologie (os, IRM neurologique et lombaire)", (2,3,3,2,2,1),
 "Rachetée par l'américain RadNet pour 230 M€ en mars 2026 ; intégrée à la filiale DeepHealth ; environ 30 M€ d'ARR, 700 clients dans 44 pays",
 "https://www.maddyness.com/2026/03/02/la-medtech-gleamer-passe-sous-pavillon-americain-pour-230-millions-deuros/",
 "Ancrage français et conformité européenne d'un groupe désormais américain", "Décisions désormais prises aux États-Unis : priorité basse", "v2",
 "Christian Allouche", "Cofondateur et CEO", "", "Reste dans l'entreprise après le rachat par RadNet", "Identifié via presse"),

("Santé", "Withings Health Solutions", "Dispositifs connectés de santé pour les professionnels", (2,3,3,3,2,3),
 "Branche professionnelle de Withings, positionnée sur la télésurveillance et la prévention",
 "", "Télésurveillance remboursée, prévention, programmes de santé publique", "Vérifier l'autonomie de la branche Health Solutions", "v2",
 "", "Direction Health Solutions", "", "", "À compléter"),
]

CIBLES += [
# ------------------------------------------------------- TRANSFORMATION (v1)
("Transformation", "Huwise (ex-Opendatasoft)", "Données publiques et pilotage pour administrations et collectivités", (3,2,0,3,2,2),
 "GovTech française la mieux financée (32,2 M$ levés à mai 2026)",
 "https://tracxn.com/d/explore/govtech-startups-in-france/", "Pilotage des politiques publiques par la donnée", "Présence aux États-Unis", "v1",
 "Jean-Marc Lazard", "Cofondateur et CEO", "https://www.linkedin.com/in/jmlazard", "Expert du Collège numérique France 2030, ancien administrateur du Cerema", "Identifié"),

("Transformation", "Manty", "Tableaux de bord et aide à la décision pour élus et agents", (3,2,1,3,1,2),
 "CEO également directeur chez Relyens (assureur du secteur public et hospitalier)",
 "", "Pilotage de l'action publique, collectivités", "Rattachement à Relyens à vérifier", "v1",
 "Harold Gerber", "CEO", "https://www.linkedin.com/in/harold-gerber", "Également directeur Risk & Product chez Relyens", "Identifié"),

("Transformation", "Hublo", "Gestion des remplacements dans les établissements de santé", (3,1,3,2,1,2),
 "Environ 200 personnes entre France, Allemagne et Espagne ; 22 M€ levés auprès de Revaia et Acton Capital",
 "", "Transformation RH de l'hôpital public, intérim médical", "Équipe publique existante à vérifier", "v1",
 "Antoine Loron", "Cofondateur et président", "https://www.linkedin.com/in/antoineloron", "Partner chez 50 Partners", "Identifié"),

("Transformation", "Cap Collectif", "Plateformes de participation citoyenne", (3,1,0,3,1,3),
 "Acteur historique de la civic tech",
 "", "Concertation, lien avec son expérience au CNR", "Petite structure (26 personnes)", "v1",
 "Cyril Lage", "CEO", "https://www.linkedin.com/in/cyril-lage-45a4967", "Ancien collaborateur parlementaire, cofondateur de Démocratie Ouverte", "Identifié"),

("Transformation", "Neocity", "Application de services pour les communes", (3,1,0,3,1,3),
 "Plus de 460 collectivités clientes",
 "", "Relation usager, collectivités", "Petite structure (25 personnes)", "v1",
 "Pierre Saulnier", "Cofondateur et président", "https://www.linkedin.com/in/saulnierpierre", "", "Identifié"),

("Transformation", "Pennylane", "Comptabilité, portée par la réforme de la facturation électronique", (3,2,0,2,1,1),
 "Scaleup de plus de 1 000 personnes",
 "", "Conduite de la réforme de la facture électronique", "Équipe affaires publiques probablement déjà en place", "v1",
 "Tancrède Besnard", "Cofondateur et CPO", "https://www.linkedin.com/in/tancrède-besnard-7b721033", "Polytechnique et Sciences Po", "Identifié"),

# ------------------------------------------------------- TRANSFORMATION (v2)
("Transformation", "Berger-Levrault", "Logiciels de gestion pour collectivités, sanitaire, médico-social et éducation", (3,2,2,3,2,2),
 "Arrivée d'un nouveau CEO le 9 mars 2026 avec un cap « AI-First » et l'objectif de doubler le chiffre d'affaires d'ici 2030 (148 M€ de CA en 2024)",
 "https://www.berger-levrault.com/fr/communique-de-presse/herve-solus-est-nomme-ceo-du-groupe-berger-levrault/",
 "Transformation IA du logiciel public, collectivités, secteur médico-social",
 "Changement de direction récent : fenêtre favorable pour proposer une fonction affaires publiques dans le nouveau projet", "v2",
 "Hervé Solus", "CEO (depuis mars 2026)", "", "Cofondateur de DigitalRecruiters, ex-comité exécutif de Cegid ; arrivé en mars 2026", "Identifié via presse"),

("Transformation", "MGDIS", "Logiciels de pilotage des politiques publiques et des aides", (3,2,0,3,1,3),
 "Cofondateur de l'association France GovTech ; 199 salariés",
 "https://www.mgdis.fr/mgdis-cofondateur-france-govtech-numerique-public-interoperable/",
 "Gestion des aides publiques, interopérabilité, France GovTech", "Actionnariat et gouvernance à vérifier", "v2",
 "Franck Mosser", "CEO", "https://www.linkedin.com/in/franck-mosser-4202475", "Dirige MGDIS, cofondateur de France GovTech, basé à Vannes", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Ciril Group", "Logiciels et cloud pour les collectivités locales", (3,2,1,3,1,3),
 "323 salariés ; activité cloud dédiée au secteur public",
 "", "Numérique des collectivités, cybersécurité des territoires", "Vérifier l'existence d'une fonction relations institutionnelles", "v2",
 "Rémi Grivel", "Directeur général", "https://www.linkedin.com/in/grivel-rémi-1655a529", "Directeur général, président du CLUSIR Auvergne-Rhône-Alpes", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Groupe JVS", "Logiciels pour les communes et les collectivités", (3,1,0,3,1,3),
 "334 salariés ; forte base de petites communes",
 "", "Numérique des petites communes, mutualisation intercommunale", "Vérifier l'appétence pour une fonction affaires publiques", "v2",
 "Yann Duverdier", "Directeur général", "https://www.linkedin.com/in/yduverdier", "Directeur général du groupe, basé à Reims", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Arpège", "Logiciels d'état civil et de relation citoyen pour les communes", (3,1,0,3,1,3),
 "331 salariés ; acteur historique de l'état civil et de la relation usager",
 "", "Relation usager, dématérialisation de l'état civil, identité numérique", "Structure familiale : vérifier l'appétence pour un poste affaires publiques", "v2",
 "Bruno Bertheleme", "PDG", "https://www.linkedin.com/in/bruno-bertheleme-9a889310b", "PDG, basé à Nantes", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Localeo", "Relation usager et démarches en ligne pour les collectivités", (3,1,0,3,1,3),
 "Positionnement relation usager et guichet unique pour les collectivités",
 "", "Relation usager, France Services, dématérialisation", "Effectif, actualité 2026 et dirigeant à vérifier", "v2",
 "", "Direction générale", "", "", "À compléter"),

("Transformation", "Docaposte", "Numérique de confiance pour l'État, les collectivités et la santé (groupe La Poste)", (3,2,2,3,2,1),
 "Chef de file de NumSpot (cloud souverain) avec la Banque des Territoires, Dassault Systèmes et Bouygues Telecom",
 "https://www.docaposte.com/presse/communique-de-presse/numspot-retour-sur-une-premiere-annee-riche",
 "Souveraineté numérique, hébergement de données de santé, identité numérique",
 "Filiale d'un grand groupe public : affaires publiques déjà portées par La Poste", "v2",
 "Olivier Vallet", "PDG", "", "PDG de Docaposte, porte-parole de la souveraineté numérique française", "Identifié via presse"),

("Transformation", "Make.org", "Participation citoyenne et consultations à grande échelle", (3,2,1,3,1,3),
 "Plateforme Panoramic développée avec le CESE pour restituer les travaux de la convention citoyenne grâce à l'IA ; 60 salariés",
 "https://about.make.org/post/convention-citoyenne-sur-la-fin-de-vie-le-cese-avec-make-org-propose-au-grand-public-et-aux-parlementaires-de-mieux-sapproprier-les-debats-des-citoyens-grace-a-lintelligence-artificielle",
 "Concertation nationale, CNR, conventions citoyennes : correspondance directe avec son expérience",
 "Structure mixte entreprise/fondation : clarifier quelle entité recruterait", "v2",
 "Axel Dauchez", "Président et cofondateur", "", "Ancien dirigeant de Deezer, porte le discours public sur la démocratie participative", "Identifié via presse"),

("Transformation", "Fluicity", "Plateforme de concertation et de participation locale", (3,1,0,3,1,3),
 "Positionnement concertation locale pour collectivités et opérateurs",
 "", "Concertation réglementaire, acceptabilité des projets locaux", "Effectif, actualité 2026 et dirigeant à vérifier", "v2",
 "", "Direction générale", "", "", "À compléter"),

("Transformation", "Ecov", "Lignes de covoiturage sans réservation pour les collectivités", (3,2,0,3,2,3),
 "Retenue par Île-de-France Mobilités (accord-cadre pouvant aller jusqu'à 8 ans) pour le plateau de Saclay et une vingtaine de lignes en grande couronne ; également retenue par les Hauts-de-France ; 146 salariés",
 "https://www.auto-infos.fr/article/ecov-chantre-du-covoiturage-en-ile-de-france.285278",
 "Autorités organisatrices de la mobilité, marchés publics, décarbonation des mobilités rurales",
 "Entreprise de l'économie sociale et solidaire : vérifier le niveau de rémunération possible", "v2",
 "Thomas Matagne", "Président et cofondateur", "https://www.linkedin.com/in/thomasmatagne", "Diplômé de Sciences Po, fondateur d'une entreprise de l'ESS", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Vianova", "Plateforme de données de mobilité pour les villes et les opérateurs", (3,3,0,3,2,3),
 "Plus de 150 villes, opérateurs et entreprises clients en Europe, au Moyen-Orient et en Océanie",
 "https://vianova.io/blog/vianova-raises-eu6-million-to-make-global-transport-safer-greener-and-more-efficient-through-its-collaborative-mobility-data-platform",
 "Régulation des mobilités partagées, données publiques, villes", "Dernière levée et effectif 2026 à vérifier", "v2",
 "Thibaud Febvre", "Cofondateur et COO", "https://www.linkedin.com/in/thibaudfebvre", "Cofondateur, ancien de Google", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Deepki", "Données ESG et trajectoire énergétique des parcs immobiliers", (3,3,0,3,3,2),
 "Acquisition de la britannique Camion (IA appliquée à l'électrification des bâtiments) le 30 juillet 2026, quatrième acquisition depuis 2022 ; 420 salariés",
 "https://www.veilledepresse.com/entreprise/5975-deepki-le-champion-francais-de-lesg-immobilier-qui-muscle-son-ia-par-la-croissance-externe",
 "Décret tertiaire, CSRD, patrimoine immobilier public", "Vérifier l'existence d'une fonction affaires publiques et le poids du marché public", "v2",
 "Vincent Bryant", "Cofondateur et CEO", "https://www.linkedin.com/in/vincentbryant1", "Cofondateur, dirige une entreprise présente dans six pays", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Unowhy (SQOOL)", "Solutions numériques éducatives souveraines pour les collectivités", (3,2,0,3,2,3),
 "Plus de 400 collectivités accompagnées, 2 000 établissements équipés, plus d'un million d'élèves et d'enseignants ; 155 à 200 collaborateurs",
 "https://www.unowhy.com/entreprise-unowhy/", "Souveraineté numérique éducative, équipement des régions et départements, cybersécurité des collectivités",
 "Discours souveraineté déjà très construit : proposer la traduction en stratégie d'influence", "v2",
 "Jean-Yves Hepp", "Président fondateur", "https://www.linkedin.com/in/jean-yves-hepp-51a4534", "Président fondateur, porte publiquement le sujet de la souveraineté numérique éducative", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "EvidenceB", "Apprentissage adaptatif fondé sur les sciences cognitives", (3,3,0,3,1,3),
 "Intervention à l'UNESCO (Digital Learning Week, 8-11 septembre 2026) avec le ministère ivoirien de l'Éducation ; évaluation d'impact conduite par la Banque mondiale ; déploiement AdaptivMath en France et aux États-Unis",
 "https://www.linkedin.com/in/catherine-de-vulpillières-63a77013a",
 "Éducation nationale, IA en éducation, bailleurs internationaux", "Structure de 23 personnes : vérifier la capacité à financer un poste senior", "v2",
 "Thierry de Vulpillières", "CEO", "https://www.linkedin.com/in/vulpillieres", "Dirige EvidenceB ; l'entreprise intervient aux côtés du ministère de l'Éducation nationale", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Predictice", "Analyse prédictive et IA appliquées à la jurisprudence", (3,3,0,2,2,3),
 "Acteur pionnier de la justice prédictive en France, dans un marché legaltech porté par l'open data des décisions de justice",
 "https://zevra.tech/es/legaltech", "Open data de la justice, ministère de la Justice, professions réglementées", "Actualité 2026, effectif et dirigeant à vérifier", "v2",
 "", "CEO", "", "", "À compléter"),

("Transformation", "Doctrine", "Moteur de recherche juridique et IA appliquée au droit", (3,3,0,2,3,2),
 "Legaltech française la mieux financée (entrée de Summit Partners, 120 M€) ; acquisition de Maite.ai en 2025 ; 310 salariés",
 "https://zevra.tech/es/legaltech", "Open data des décisions de justice, accès au droit, régulation de l'IA juridique",
 "Vérifier si une fonction affaires publiques existe déjà", "v2",
 "Guillaume Carrère", "CEO", "https://www.linkedin.com/in/guillaume-carrère-7aaa5920", "Dirige Doctrine", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Whaller", "Plateforme collaborative souveraine pour les organisations publiques", (3,2,0,3,1,3),
 "Positionnement cloud de confiance et alternative européenne aux suites américaines pour les administrations",
 "https://fr.wikipedia.org/wiki/Thomas_Fauré", "Souveraineté numérique, doctrine « cloud au centre » de l'État, collectivités",
 "Petite structure : vérifier la capacité à financer un poste de direction", "v2",
 "Thomas Fauré", "Président fondateur", "", "Auteur de « Après Facebook, Rebâtir », voix de la souveraineté numérique française", "Identifié via presse"),

("Transformation", "Olvid", "Messagerie chiffrée certifiée ANSSI, utilisée par les ministères", (3,2,0,2,1,3),
 "Équipe les ministères depuis décembre 2023 sur décision de la Première ministre ; usage étendu au-delà du cercle gouvernemental en 2026 (barreaux, entreprises) ; ouverture d'un store de licences le 8 avril 2026",
 "https://www.cyber-securite.fr/olvid-une-revolution-dans-la-messagerie-securisee/",
 "Souveraineté des communications de l'État, ANSSI, extension aux collectivités et aux hôpitaux",
 "17 salariés : le poste serait à construire et à dimensionner", "v2",
 "Thomas Baignères", "Cofondateur et CEO", "https://www.linkedin.com/in/baigneres", "Cryptographe, dirige la messagerie retenue par le gouvernement", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Jamespot", "Réseau social d'entreprise souverain, présent dans le secteur public", (3,2,0,2,1,3),
 "44 salariés ; positionnement souveraineté et collaboration pour les organisations publiques",
 "", "Souveraineté numérique, collaboration dans l'administration", "Petite structure : poste à dimensionner", "v2",
 "Alain Garnier", "CEO", "https://www.linkedin.com/in/garniera", "Dirigeant très présent dans le débat sur la souveraineté numérique", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Oodrive", "Confiance numérique et collaboration sécurisée (SecNumCloud)", (3,2,0,2,2,2),
 "385 salariés ; qualifications SecNumCloud et clients dans les secteurs sensibles",
 "", "Doctrine cloud de l'État, SecNumCloud, NIS2", "Vérifier l'existence d'une direction des affaires publiques", "v2",
 "", "Direction générale", "", "", "À compléter"),

("Transformation", "NumSpot", "Cloud souverain de confiance (Docaposte, Banque des Territoires, Dassault Systèmes, Bouygues Telecom)", (3,2,2,3,2,2),
 "Consortium public-privé visant la qualification SecNumCloud et la certification HDS, ciblant en priorité le secteur public, la santé et la finance ; 109 salariés",
 "https://numspot.com/2024/11/21/numspot-annonce-le-lancement-de-sa-plateforme-de-services-au-premier-trimestre-2025/",
 "Doctrine « cloud au centre », hébergement des données de santé, commande publique",
 "Gouvernance à quatre actionnaires : les relations institutionnelles peuvent être portées par les actionnaires", "v2",
 "Alain Issarni", "Président-directeur général", "", "PDG de NumSpot, ancien de la DGFiP", "Identifié via presse"),

("Transformation", "Clever Cloud", "Cloud souverain français, hébergement d'applications publiques", (3,2,0,3,2,3),
 "84 salariés ; positionnement cloud souverain français",
 "", "Doctrine cloud de l'État, souveraineté, collectivités", "Vérifier le poids réel du secteur public dans le chiffre d'affaires", "v2",
 "Cedric Biron", "COO", "https://www.linkedin.com/in/cedric-biron-68939114", "Directeur des opérations, basé à Nantes", "Identifié (FullEnrich, 09/2026)"),

("Transformation", "Dastra", "Pilotage de la conformité RGPD et gouvernance des données", (3,2,1,3,1,3),
 "47 salariés ; cofondateur ancien de la CNIL ; lauréate France Legaltech 2026",
 "https://zevra.tech/es/legaltech", "RGPD, AI Act, conformité des collectivités et des établissements publics",
 "Petite structure : poste à construire", "v2",
 "Jérôme de Mercey", "Cofondateur et COO", "https://www.linkedin.com/in/jérôme-de-mercey", "Ancien de la CNIL, cofondateur de Dastra", "Identifié (FullEnrich, 09/2026)"),
]

CIBLES += [
# ------------------------------------------------------------------- IA (v1)
("IA", "Naaia", "Conformité IA (AI Act, ISO 42001)", (2,3,2,1,3,3),
 "Série A de 6 M€ menée par Ventech (juillet 2026) ; 9 M€ levés au total ; clients CAC 40, SBF 120 et acteurs publics ; échéance du code de bonnes pratiques IA au 2 août 2026",
 "https://www.maddyness.com/2026/07/08/naaia-leve-6-millions-deuros-pour-aider-les-entreprises-a-se-conformer-a-lai-act/",
 "Ouvrir les hôpitaux et les administrations à la conformité IA", "Aucun point bloquant identifié : cible prioritaire", "v1",
 "Nathalie Beslay", "Cofondatrice et CEO", "https://www.linkedin.com/in/nathalie-beslay-843a781", "Avocate en droit de la santé, ancienne conseillère technique du secrétaire d'État à la santé", "Identifié"),

("IA", "LightOn", "IA générative souveraine pour les entreprises et le secteur public", (3,3,1,1,2,2),
 "Chiffre d'affaires du premier semestre 2026 en hausse de 51 % ; première société européenne d'IA cotée (Euronext Growth) ; offre souveraine ciblant santé, défense et secteur public",
 "https://www.webdisclosure.fr/press-release/lighton-etr-lighton-chiffre-daffaires-semestriel-2026-en-hausse-de-51-98UVUF2FJFd",
 "Ministères, hôpitaux, souveraineté ; société cotée donc lisible", "Communication sur l'horizon de trésorerie : vérifier la solidité financière avant d'accepter", "v1",
 "", "CEO", "", "Direction à identifier précisément", "À compléter"),

("IA", "Mistral AI", "LLM souverain, fournisseur de l'assistant IA de l'État", (3,3,1,2,1,1),
 "Expérimentation interministérielle lancée en octobre 2025 auprès de 10 000 agents dans plusieurs ministères ; décision de généralisation attendue courant 2026 ; 1,7 Md€ levés en septembre 2025, valorisation de 11,7 Md€",
 "https://www.lenouveleconomiste.fr/mistral-ai-face-a-son-vrai-test-letat-francais-et-le-milliard-de-revenus-136029/",
 "Généralisation de l'assistant IA de l'État et achats publics d'IA ; viser l'équipe secteur public plutôt qu'un poste d'affaires publiques généraliste",
 "Équipe affaires publiques déjà structurée", "v1",
 "", "Équipe secteur public", "", "Viser l'équipe secteur public France plutôt que la direction générale", "À compléter"),

("IA", "Giskard", "Évaluation et sécurité des modèles d'IA", (2,3,0,1,2,3),
 "Positionnement AI Act et IA de confiance ; 24 salariés",
 "", "Acheteurs publics, régulation IA", "Levée récente à vérifier", "v1",
 "Jean-Marie John-Mathews", "Cofondateur et co-CEO", "https://www.linkedin.com/in/jmjohnmathews", "Enseigne « Algorithms & Public Policy » à Sciences Po", "Identifié"),

("IA", "Gradium", "IA vocale", (1,3,0,1,3,2),
 "Levée récente ; équipe en structuration (Chief Product Officer et Chief Growth Officer en place)",
 "", "Accueil téléphonique des services publics (à construire)", "Intérêt pour le secteur public à valider", "v1",
 "Constance Grisoni Deperrois", "Chief Growth Officer", "https://www.linkedin.com/in/constance-d-g", "Porte la croissance ; point d'entrée pour tester l'appétence secteur public", "Identifié (FullEnrich, 09/2026)"),

# ------------------------------------------------------------------- IA (v2)
("IA", "Probabl", "Opérateur officiel de scikit-learn, IA open source souveraine (spin-off Inria)", (3,3,1,1,3,3),
 "13 M€ levés en amorçage (Serena, CFM, Mozilla Ventures, French Tech Souveraineté), 18,5 M€ au total : record européen pour une entreprise open source commercial ; inscrite dans la stratégie nationale IA et France 2030",
 "https://www.inria.fr/fr/probabl-logiciel-open-source-intelligence-artificielle",
 "Partenariat public-privé avec Inria, France 2030, communs numériques : correspondance directe avec son travail à la DITP",
 "Entreprise très jeune : vérifier le calendrier de structuration de l'équipe", "v2",
 "Yann Lechelle", "CEO et cofondateur", "", "Ancien dirigeant de Scaleway, voix publique de la souveraineté numérique européenne", "Identifié via presse"),

("IA", "Craft AI", "IA de confiance et industrialisation des modèles pour les organisations régulées", (3,3,2,2,2,3),
 "37 salariés ; CEO ambassadeur du programme « Osez l'IA »",
 "", "IA de confiance, AI Act, secteur public et santé", "Vérifier le poids du secteur public dans le chiffre d'affaires", "v2",
 "Homéric de Sarthe", "Directeur général", "https://www.linkedin.com/in/homericdesarthe", "Ambassadeur « Osez l'IA », distingué « 40 Under 40 »", "Identifié (FullEnrich, 09/2026)"),

("IA", "Miralia (ex-Golem.ai)", "IA symbolique et traitement automatique de documents", (3,3,0,2,1,3),
 "Changement de nom de Golem.ai en Miralia",
 "", "Traitement documentaire des administrations, IA frugale et explicable", "Taille et situation financière à vérifier après le changement de marque", "v2",
 "Guillaume Navarre", "Cofondateur et directeur général", "https://www.linkedin.com/in/guillaume-navarre", "Cofondateur, positionné sur l'IA explicable", "Identifié (FullEnrich, 09/2026)"),

("IA", "Lettria", "Traitement du langage et graphes de connaissances en français", (2,3,0,1,2,3),
 "21 salariés ; positionnement NLP souverain",
 "", "Traitement documentaire des administrations, souveraineté linguistique", "Poids du secteur public à valider", "v2",
 "Charles Borderie", "Cofondateur et CEO", "https://www.linkedin.com/in/charlesborderie", "Cofondateur et CEO", "Identifié (FullEnrich, 09/2026)"),

("IA", "Sinequa (ChapsVision)", "Recherche et IA documentaire d'entreprise, déployée dans les administrations", (3,3,0,2,2,1),
 "Intégrée au groupe ChapsVision ; 136 salariés",
 "", "Recherche d'information dans les ministères, souveraineté", "Filiale : les affaires publiques sont portées par ChapsVision", "v2",
 "Dominique Nadeau", "Directeur des opérations", "https://www.linkedin.com/in/dominique-nadeau-b9b1115", "Directeur des opérations de Sinequa", "Identifié (FullEnrich, 09/2026)"),

("IA", "Dust", "Agents IA d'entreprise connectés aux données internes", (1,3,1,1,3,3),
 "40 M$ levés en série B (Sequoia, Abstract), plus de 60 M$ au total ; plus de 3 000 organisations, 41 000 utilisateurs actifs mensuels, 300 000 agents déployés (avril 2026)",
 "https://www.qore.com/ai/dust-levanta-40-mdd-para-llevar-la-ia-colaborativa-a-las-empresas/",
 "Déploiement d'agents IA dans l'administration : marché à créer, correspond à son travail sur les cas d'usage IA de l'État",
 "Positionnement franco-américain et privé : l'appétence secteur public est à construire", "v2",
 "Gabriel Hubert", "Cofondateur et CEO", "", "Ancien de Stripe, cofondateur avec Stanislas Polu", "Identifié via presse"),

("IA", "Linagora", "Logiciel libre et IA générative souveraine (LucIE, Twake)", (3,3,0,2,1,3),
 "142 salariés ; positionnement logiciel libre souverain pour l'État",
 "", "Logiciel libre dans l'administration, souveraineté, alternatives aux suites américaines", "Vérifier la solidité financière et le modèle économique", "v2",
 "Alexandre Zapolsky", "Président fondateur", "https://www.linkedin.com/in/alexandrezapolsky", "Fondateur, très engagé publiquement sur la souveraineté numérique", "Identifié (FullEnrich, 09/2026)"),

("IA", "Hugging Face", "Plateforme de modèles d'IA open source", (1,3,1,1,3,2),
 "Entreprise française de référence mondiale sur l'IA open source",
 "", "IA open source, communs numériques, régulation européenne", "Centre de gravité américain : vérifier l'existence d'un poste France/Europe", "v2",
 "", "Direction Europe", "", "", "À compléter"),

("IA", "Wintics", "Analyse vidéo par IA pour les collectivités et les infrastructures de transport", (3,3,0,3,2,3),
 "Titulaire de deux des quatre lots du marché d'État de vidéoprotection algorithmique (Île-de-France et transports) ; plus de 34 collectivités clientes dont Paris, Nice et la Loire-Atlantique ; bénéficie de l'assouplissement du cadre réglementaire après les JO",
 "https://x-pression.media/videosurveillance-algorithmique-la-start-up-francaise-wintics-beneficie-de-lassouplissement-reglementaire",
 "Cadre légal de la vidéoprotection algorithmique, préfectures, collectivités : sujet d'affaires publiques par excellence",
 "19 salariés : le poste serait le premier du genre, à dimensionner", "v2",
 "Quentin Barenne", "Cofondateur", "https://www.linkedin.com/in/quentinbarenne", "Porte le discours public sur l'encadrement éthique de l'analyse vidéo", "Identifié (FullEnrich, 09/2026)"),

("IA", "Videtics", "Analyse vidéo par IA pour la sécurité et la gestion urbaine", (3,3,0,3,1,3),
 "Titulaire du lot 2 du marché d'État de vidéoprotection algorithmique (PACA, Rhône-Alpes, Outre-mer, Corse) ; 20 salariés",
 "https://www.faceaurisque.com/2024/04/15/la-videoprotection-algorithmique-se-deploie-l-approche-des-jop-2024/",
 "Pérennisation du cadre légal de la vidéoprotection algorithmique, collectivités", "Très petite structure : poste à construire", "v2",
 "Alexandre Reboul", "Cofondateur et CTO", "https://www.linkedin.com/in/alexandre-reboul-a5530386", "Cofondateur, basé à Nice", "Identifié (FullEnrich, 09/2026)"),

("IA", "XXII", "Vision par ordinateur et IA appliquée à la vidéo", (3,3,0,3,2,3),
 "377 salariés ; positionnement IA de vision pour les villes et les infrastructures",
 "", "Encadrement de la vidéoprotection algorithmique, collectivités, industrie", "Situation financière 2026 à vérifier", "v2",
 "William Eldin", "CEO", "https://www.linkedin.com/in/william-eldin", "Dirigeant très présent médiatiquement sur l'IA et la sécurité", "Identifié (FullEnrich, 09/2026)"),

("IA", "ChapsVision", "Traitement et exploitation massive de données pour le régalien", (3,3,0,2,3,2),
 "Retenue en juin 2026 pour succéder à Palantir à la DGSI, avec un périmètre couvrant DGSI, douanes, police et gendarmerie ; transition estimée entre un et trois ans ; solution également retenue par les services allemands",
 "https://cyberveille.ch/tags/dgsi/", "Souveraineté du renseignement, commande publique régalienne, acceptabilité politique",
 "Groupe déjà très introduit auprès de l'État : vérifier s'il existe une direction des affaires publiques", "v2",
 "Olivier Dellenbach", "PDG", "", "PDG, a qualifié le contrat DGSI d'« immense victoire pour ChapsVision et pour l'Europe »", "Identifié via presse"),

("IA", "Filigran", "Cybersécurité open source (OpenCTI, OpenBAS)", (3,3,0,2,3,3),
 "58 M$ levés en série C (octobre 2025), plus de 100 M$ au total : plus grosse levée de la cybersécurité française ; plus de 6 000 organisations utilisatrices dont la Commission européenne, l'ANSSI et le FBI ; objectif de doubler voire tripler les effectifs en 2026",
 "https://les-smartgrids.fr/filigran-levee-de-fonds-cybersecurite-france/",
 "Souveraineté cyber, coopération européenne, agences publiques : le CEO vient lui-même de l'ANSSI",
 "Expansion internationale forte : vérifier si le poste serait France ou Europe", "v2",
 "Samuel Hassine", "Cofondateur et CEO", "", "Ancien responsable du bureau Analyse de la menace de l'ANSSI", "Identifié via presse"),

("IA", "HarfangLab", "EDR souverain certifié et qualifié par l'ANSSI", (3,3,0,2,3,3),
 "Premier EDR certifié et qualifié par l'ANSSI ; plus de 250 clients dont des administrations et des secteurs sensibles ; extension de la plateforme (EPP, Attack Surface Management) et fonctionnalités de conformité déployées début 2026",
 "https://harfanglab.io/fr/press/harfanglab-integre-lattack-surface-management-a-sa-plateforme-de-cybersecurite-des-terminaux/",
 "NIS2, qualification ANSSI, cybersécurité des collectivités et des hôpitaux", "Vérifier l'existence d'une fonction relations institutionnelles", "v2",
 "Grégoire Germain", "Cofondateur et CEO", "", "Cofondateur, a construit l'alternative souveraine française aux EDR étrangers", "Identifié via presse"),

("IA", "Sekoia.io", "Plateforme AI-SOC souveraine de détection et de réponse", (3,3,0,2,3,3),
 "26 M€ levés en série B (Revaia, UNEXO, Bpifrance), 60 M€ au total ; clients EDF, SNCF, Vinci et ministère des Armées ; plus de cent salariés",
 "https://dynamciwebdevelopment.com/sekoia-renforce-sa-position-en-cybersecurite-avec-une-levee-de-fonds-de-26-millions-deuros/",
 "NIS2, cybersécurité des opérateurs publics, souveraineté", "Modèle indirect via les MSSP : vérifier le poids du marché public direct", "v2",
 "Freddy Milesi", "CEO", "", "Dirige Sekoia.io, présente dans quatre pays européens", "Identifié via presse"),

("IA", "Gatewatcher", "Détection des menaces réseau (NDR) souveraine", (3,3,0,2,2,3),
 "102 salariés ; positionnement souverain auprès des opérateurs d'importance vitale",
 "", "NIS2, OIV, qualification ANSSI", "Vérifier l'existence d'une fonction affaires publiques", "v2",
 "Jacques de La Rivière", "CEO", "https://www.linkedin.com/in/jacques-de-la-rivière-77921b5", "Cofondateur et dirigeant", "Identifié (FullEnrich, 09/2026)"),

("IA", "Tehtris", "Plateforme XDR souveraine", (3,3,0,2,2,3),
 "123 salariés ; positionnement XDR européen",
 "", "NIS2, souveraineté cyber, collectivités", "Changement de direction récent : vérifier la stratégie", "v2",
 "Richard Vacher Detourniere", "Directeur général", "https://www.linkedin.com/in/rvacherdetourniere", "Dirigeant, profil transformation d'entreprises technologiques", "Identifié (FullEnrich, 09/2026)"),

("IA", "GLIMPS", "Détection avancée de logiciels malveillants par IA", (3,3,0,2,2,3),
 "63 salariés ; technologie issue de la communauté cyber de Rennes, proche du ministère des Armées",
 "", "Souveraineté cyber, ministère des Armées, qualification ANSSI", "Petite structure : poste à dimensionner", "v2",
 "Coralie Heritier", "Directrice générale", "https://www.linkedin.com/in/coralie-heritier", "Directrice générale de GLIMPS", "Identifié (FullEnrich, 09/2026)"),

("IA", "Comand AI", "Logiciels d'aide au commandement militaire (suite Prevail)", (3,3,0,1,3,3),
 "Fondée en 2023, équipe issue de Palantir, d'OpenAI et du ministère des Armées ; 8,5 M€ levés ; 37 salariés",
 "https://blog.forinov.com/secteurs-dinnovations/comand-ai-leve-85-me-pour-revolutionner-la-defense-avec-lia/2944/",
 "Ministère des Armées, loi de programmation militaire, achats de défense", "Marché quasi exclusivement étatique : l'accès aux décideurs est le cœur du poste", "v2",
 "Loïc Mougeolle", "Cofondateur et CEO", "https://www.linkedin.com/in/loïc-mougeolle", "Cofondateur et CEO", "Identifié (FullEnrich, 09/2026)"),

("IA", "Harmattan AI", "IA et systèmes autonomes pour la défense", (3,3,0,1,3,3),
 "200 M$ levés en 2026 pour une valorisation de 1,4 Md€, avec Dassault Aviation, Bpifrance et Future French Champions au capital ; intégration visée dans le Rafale F5 et les drones de combat ; 190 salariés",
 "https://altusentreprise.com/harmattan-ai-defense-francaise/",
 "Loi de programmation militaire, souveraineté, relations avec le ministère des Armées",
 "Croissance très rapide : vérifier l'organisation des relations institutionnelles (la COO est passée par l'ENA)", "v2",
 "Lucile Poivert", "COO", "https://www.linkedin.com/in/lucile-poivert-6119b3335", "COO, HEC et ENA : interlocutrice naturelle pour un profil affaires publiques", "Identifié (FullEnrich, 09/2026)"),

("IA", "Unseenlabs", "Renseignement spatial d'origine électromagnétique", (3,3,0,1,3,3),
 "107 salariés ; clients étatiques (marines, agences) en Europe et à l'international",
 "", "Souveraineté spatiale, surveillance maritime, ministère des Armées", "Entreprise rennaise : vérifier la localisation du poste", "v2",
 "Clément Galic", "Cofondateur et CEO", "https://www.linkedin.com/in/clément-galic-633825a5", "Cofondateur et CEO, basé à Rennes", "Identifié (FullEnrich, 09/2026)"),

("IA", "Delair", "Drones et IA pour la défense, l'énergie et les infrastructures", (3,3,0,2,2,3),
 "259 salariés ; positionnement dual défense et infrastructures critiques",
 "", "Loi de programmation militaire, réglementation des drones, infrastructures publiques", "Vérifier l'existence d'une fonction affaires publiques", "v2",
 "Bastien Mancini", "CEO", "https://www.linkedin.com/in/bastien-mancini-199749137", "Dirige Delair, basé à Toulouse", "Identifié (FullEnrich, 09/2026)"),
]

# --------------------------------------------------------------------------
# Calibrage des notes v2 sur les ancres de la v1.
#
# La v1 réservait un 3 en « stade et levée » aux levées importantes et
# récentes, et un 3 en « poste à créer » aux structures de moins d'une
# soixantaine de personnes sans fonction affaires publiques. La première
# version de ce fichier était trop généreuse : 76 % des cibles ressortaient
# en priorité haute contre 42 % dans la v1. Les notes ci-dessous rétablissent
# cette calibration. Elles restent modifiables dans le classeur.
# --------------------------------------------------------------------------

CALIBRAGE = {
    # Santé
    "Doctolib": (2,3,3,3,1,0), "Lifen": (3,2,3,3,1,2), "Arkhn": (3,3,3,3,1,3),
    "Galeon": (3,3,3,3,1,2), "Sancare": (3,3,3,2,1,2), "Implicity": (3,3,3,2,3,2),
    "Omnidoc": (3,2,3,3,1,3), "Incepto Medical": (3,3,3,3,1,2), "Milvue": (2,3,3,3,1,2),
    "Raidium": (3,3,3,2,1,3), "TheraPanacea": (3,3,3,2,1,3), "Kiro": (3,3,3,2,1,3),
    "Synapse Medicine": (3,3,3,2,1,2), "Posos": (3,3,3,1,1,3), "Resilience": (3,2,3,3,1,2),
    "Cureety": (3,2,3,3,1,2), "Tilak Healthcare": (3,2,3,2,1,3), "Poppins": (3,2,3,2,1,3),
    "Ludocare": (3,2,3,1,1,2), "Lucine": (3,2,3,1,1,2), "Ambler": (3,2,3,3,1,2),
    "Ambuliz": (3,1,3,2,1,2), "Happytal": (3,1,3,3,1,1), "Medaviz": (3,1,3,3,1,2),
    "Nouveal e-santé": (3,1,3,2,1,2), "Exolis": (3,1,3,2,1,2), "BioSerenity": (2,3,3,2,1,2),
    "Wandercraft": (3,3,3,1,3,2), "FeetMe": (3,2,3,1,1,2), "Softway Medical": (3,2,3,3,2,1),
    "Maincare": (3,2,3,3,1,1), "Enovacom": (3,2,3,3,1,0), "Weda": (2,2,3,3,1,1),
    "Medadom": (3,2,3,3,2,2), "Qare": (3,2,3,3,1,0), "Alan": (3,3,3,3,2,1),
    "Owkin": (3,3,3,1,3,1), "Bioptimus": (2,3,3,1,2,2), "Gleamer": (2,3,3,1,1,0),
    "Withings Health Solutions": (2,2,3,2,1,2),
    # Transformation
    "Berger-Levrault": (3,2,2,3,2,2), "MGDIS": (3,2,0,3,1,2), "Ciril Group": (3,2,1,3,1,2),
    "Groupe JVS": (3,1,0,3,1,2), "Arpège": (3,1,0,3,1,2), "Localeo": (3,1,0,3,1,2),
    "Docaposte": (3,2,2,3,2,0), "Make.org": (3,2,1,3,1,3), "Fluicity": (3,1,0,3,1,3),
    "Ecov": (3,2,0,3,2,3), "Vianova": (3,3,0,3,1,2), "Deepki": (2,3,0,3,2,1),
    "Unowhy (SQOOL)": (3,2,0,3,2,2), "EvidenceB": (3,3,0,3,1,3), "Predictice": (3,3,0,2,1,3),
    "Doctrine": (2,3,0,2,2,1), "Whaller": (3,2,0,3,1,3), "Olvid": (3,2,0,2,1,3),
    "Jamespot": (3,2,0,2,1,2), "Oodrive": (3,2,0,2,1,1), "NumSpot": (3,2,2,3,2,1),
    "Clever Cloud": (2,2,0,3,1,2), "Dastra": (2,2,1,2,1,3),
    # IA
    "Probabl": (3,3,1,1,3,3), "Craft AI": (2,3,2,2,1,3), "Miralia (ex-Golem.ai)": (3,3,0,2,1,3),
    "Lettria": (2,3,0,1,1,3), "Sinequa (ChapsVision)": (3,3,0,2,1,0), "Dust": (1,3,1,1,3,2),
    "Linagora": (3,3,0,2,1,3), "Hugging Face": (1,3,1,1,3,1), "Wintics": (3,3,0,3,2,3),
    "Videtics": (3,3,0,3,1,3), "XXII": (3,3,0,3,1,2), "ChapsVision": (3,3,0,2,3,1),
    "Filigran": (3,3,0,2,3,2), "HarfangLab": (3,3,0,2,2,2), "Sekoia.io": (3,3,0,2,2,2),
    "Gatewatcher": (3,3,0,2,1,2), "Tehtris": (3,3,0,2,1,2), "GLIMPS": (3,3,0,2,1,3),
    "Comand AI": (3,3,0,1,2,3), "Harmattan AI": (3,3,0,1,3,2), "Unseenlabs": (3,3,0,1,2,2),
    "Delair": (3,3,0,2,1,2),
}

CIBLES = [
    c[:3] + (CALIBRAGE.get(c[1], c[3]),) + c[4:]
    for c in CIBLES
]

# Les notes de la v1 ne sont jamais modifiées : contrôle de non-régression.
assert all(e not in CALIBRAGE for e in
           (c[1] for c in CIBLES if c[8] == "v1")), "le calibrage ne doit porter que sur les ajouts v2"
