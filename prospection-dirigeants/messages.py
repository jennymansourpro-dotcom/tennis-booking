# -*- coding: utf-8 -*-
"""Génération des messages LinkedIn personnalisés pour chaque cible.

Deux formats par dirigeant :
  - une note de connexion (contrainte LinkedIn : 300 caractères maximum) ;
  - un premier message long, à envoyer après acceptation ou en InMail.

Règle importante : les colonnes « Angle pour Mehdi » et « Points à vérifier »
du classeur sont des notes internes. Seule la partie de l'angle située avant
le « : » ou le « ; » est reprise dans les messages, pour ne jamais envoyer au
destinataire un commentaire écrit pour Mehdi.
"""

import re

LIMITE_NOTE = 300

PREUVE = {
    "Santé": ("j'ai coordonné le déploiement national des réformes santé auprès des préfectures "
              "et des cabinets ministériels, et piloté les partenariats public-privé "
              "(Salesforce, Apple) de la campagne de vaccination"),
    "Transformation": ("j'ai dirigé le développement d'une application métier utilisée par "
                       "10 000 agents publics et coordonné l'ensemble des ministères impliqués "
                       "au Conseil national de la refondation"),
    "IA": ("j'ai défini et déployé la feuille de route IA des services publics, du cadrage "
           "des priorités à la mise en œuvre dans les ministères"),
}

PITCH = {
    "Santé": "je sais généraliser une solution sur le territoire et sécuriser son financement",
    "Transformation": "je sais comment l'administration achète, décide et conduit le changement",
    "IA": "j'ai écrit la stratégie IA de l'État, je sais ce qu'attendent les acheteurs publics",
}


MOTS_OUTILS = {
    "de", "du", "des", "d", "le", "la", "les", "un", "une", "et", "ou", "à", "au", "aux",
    "en", "dans", "sur", "pour", "par", "avec", "sans", "chez", "vers", "dont", "que", "qui",
    "pouvant", "visant", "ainsi", "plus", "son", "sa", "ses", "leur", "leurs", "notamment",
    "est", "sont", "cap", "lors",
}


def _tronque(texte, maxlen):
    """Coupe proprement : jamais au milieu d'un nombre ni sur un mot-outil."""
    texte = re.sub(r"\s+", " ", texte).strip()
    if len(texte) <= maxlen:
        return texte.rstrip(" .,;:—-")
    coupe = texte[:maxlen]
    for sep in (", ", " — ", " ("):
        if sep in coupe and len(coupe.rsplit(sep, 1)[0]) > maxlen * 0.5:
            coupe = coupe.rsplit(sep, 1)[0]
            break
    else:
        coupe = coupe.rsplit(" ", 1)[0]
    coupe = coupe.rstrip(" .,;:—-(«\u00bb\"'")
    # on ne termine jamais sur un mot-outil (« ... du marché d'État de »)
    mots = coupe.split()
    while len(mots) > 3 and mots[-1].lower().rstrip("'").strip("(") in MOTS_OUTILS:
        mots.pop()
    # une parenthèse ouverte et non refermée est retirée
    coupe = " ".join(mots).rstrip(" .,;:—-")
    if coupe.count("(") > coupe.count(")"):
        coupe = coupe[:coupe.rindex("(")].rstrip(" .,;:—-")
    return coupe


def accroche(signal, maxlen=120):
    """Réduit le signal d'actualité à une accroche courte et lisible."""
    if not signal:
        return ""
    return _tronque(signal.split(" ; ")[0], maxlen)


def sujet(angle, maxlen=60, complet=False):
    """Extrait de l'angle la partie présentable au destinataire.

    `complet=False` ne garde que le premier syntagme, pour tenir dans la note
    de connexion ; `complet=True` garde l'énumération pour le message long.
    """
    if not angle:
        return "vos sujets publics"
    texte = re.split(r" : | ; ", angle)[0]
    if not complet:
        texte = texte.split(",")[0]
    return _tronque(texte, maxlen)


def prenom_de(nom):
    return nom.split()[0] if nom else "{Prénom}"


def _minuscule(texte):
    """Passe la première lettre en minuscule, sauf si le mot est un nom propre."""
    if not texte:
        return texte
    premier = texte.split()[0].strip("(")
    if premier.isupper() or premier in NOMS_PROPRES:
        return texte
    return texte[0].lower() + texte[1:]


NOMS_PROPRES = {"Île-de-France", "France", "Inria", "Ségur", "Palantir", "Renault",
                "Dassault", "Microsoft", "Bpifrance", "Ramsay", "Gustave", "Doctolib"}


def note_connexion(cible):
    """Note de connexion LinkedIn, garantie sous la limite de 300 caractères."""
    prenom = prenom_de(cible["nom"])
    entreprise = cible["entreprise"].split(" (")[0]
    theme = _minuscule(sujet(cible["angle"], 60))

    for longueur in (95, 75, 60, 45):
        hook = accroche(cible["signal"], longueur)
        if not hook:
            break
        texte = (f"Bonjour {prenom}, j'ai suivi votre actualité — {_minuscule(hook)}. "
                 f"Conseiller stratégie IA à la "
                 f"DITP, je fais le lien entre une solution et la décision publique — et le sujet "
                 f"{theme} chez {entreprise} m'intéresse. Ravi d'échanger.")
        if len(texte) <= LIMITE_NOTE:
            return texte

    replis = [
        (f"Bonjour {prenom}, conseiller stratégie IA à la DITP après sept ans en cabinets "
         f"ministériels, j'accompagne le passage à l'échelle des solutions dans la sphère publique. "
         f"Le sujet {theme} chez {entreprise} m'intéresse particulièrement. Au plaisir d'échanger."),
        (f"Bonjour {prenom}, conseiller stratégie IA à la DITP, j'accompagne le passage à l'échelle "
         f"des solutions dans la sphère publique. Le sujet {theme} chez {entreprise} m'intéresse. "
         f"Au plaisir d'échanger."),
        (f"Bonjour {prenom}, conseiller stratégie IA à la DITP. Le sujet {theme} chez {entreprise} "
         f"m'intéresse beaucoup. Au plaisir d'échanger."),
    ]
    for texte in replis:
        if len(texte) <= LIMITE_NOTE:
            return texte
    return replis[-1][:LIMITE_NOTE - 1].rsplit(" ", 1)[0] + "."


def message_long(cible):
    prenom = prenom_de(cible["nom"])
    entreprise = cible["entreprise"].split(" (")[0]
    hook = accroche(cible["signal"], 200)
    theme = _minuscule(sujet(cible["angle"], 140, complet=True))
    famille = cible["famille"]

    ouverture = (f"J'ai suivi l'actualité de {entreprise} — {_minuscule(hook)}. "
                 f"C'est ce qui m'a donné envie de vous écrire."
                 if hook else
                 f"Je suis de près ce que construit {entreprise}, et c'est ce qui m'a donné "
                 f"envie de vous écrire.")

    return f"""Bonjour {prenom},

{ouverture}

Je suis conseiller stratégie IA à la Direction interministérielle de la transformation publique, après sept ans au cœur de la décision publique — chef de cabinet du Conseil national de la refondation, chef du pôle réseaux territoriaux de la task force vaccination, chef de cabinet adjoint au cabinet du secrétaire d'État chargé des retraites. Concrètement, {PREUVE[famille]}.

Chez {entreprise}, le sujet qui me paraît décisif est {theme}. C'est précisément le type de sujet que j'ai appris à faire aboutir : {PITCH[famille]}.

Si vous ouvrez, ou si vous vous posez la question d'ouvrir, un poste d'affaires publiques ou de partenariats publics, je serais heureux d'en parler vingt minutes. Et si ce n'est pas d'actualité aujourd'hui, je reste disponible pour échanger sur le sujet.

Bien à vous,
Mehdi Kellal — mehdi.kellal@gmail.com"""
