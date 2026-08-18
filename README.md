# tennis-booking — routine de réservation Paris Tennis

Réserve automatiquement chaque semaine le créneau **mercredi 19h, court 2, Tennis
Edouard Pailleron (Paris 19e)** sur tennis.paris.fr, puis envoie l'invitation par
mail et l'ajoute au calendrier.

## 1. Environnement cloud

Créer (ou réutiliser) un environnement Claude Code sur le web avec **accès réseau
« Complet »** (le script doit joindre `tennis.paris.fr` et `v70-auth.paris.fr`).

## 2. Variables d'environnement

Configurer dans l'environnement (ou un fichier `.env` local, jamais committé) :

```bash
# Identifiants Mon Paris (obligatoires)
PARIS_TENNIS_EMAIL=...
PARIS_TENNIS_PASSWORD=...

# Cible (valeurs par défaut indiquées)
TENNIS_PARTNER_FIRSTNAME=Mehdi
TENNIS_PARTNER_LASTNAME=Kellal
TENNIS_SITE_NAME=Edouard Pailleron
TENNIS_ARRONDISSEMENT=19
TENNIS_COURT=2
TENNIS_START_HOUR=19
TENNIS_WEEKDAY=2            # 0=lundi … 2=mercredi
TENNIS_OPEN_AT=08:00:00     # heure de Paris
TENNIS_DEADLINE_MINUTES=6

# Modes de test
DRY_RUN=0                   # 1 = s'arrêter avant la validation finale
SKIP_WAIT=0                 # 1 = ne pas attendre 08:00 (calage)
```

## 3. Installation

```bash
bash setup.sh
```

(installe `playwright` + `python-dotenv`, puis Chromium via
`python -m playwright install --with-deps chromium`.)

## 4. Création de la routine

1. Connecter les **connecteurs Gmail et Google Calendar** au compte Claude.
2. Créer une routine planifiée qui exécute le contenu de `ROUTINE_PROMPT.md`
   dans cet environnement.
3. Planification : **jeudi 07:52 heure de Paris**, soit en cron UTC :
   - heure d'été (CEST, UTC+2) : `52 5 * * 4`
   - heure d'hiver (CET, UTC+1) : `52 6 * * 4`
   (ajuster au changement d'heure, ou utiliser un planificateur qui accepte
   directement le fuseau Europe/Paris.)

Le script attend lui-même 08:00:00.000 précises — le cron à 07:52 sert juste à
démarrer la session, se connecter et se positionner sur le planning.

## 5. Test à blanc

Avant d'armer la routine :

```bash
DRY_RUN=1 SKIP_WAIT=1 python book_tennis.py
cat out/result.json
```

Attendu : `status: "dry_run"` et les captures `01_landing` → `10_partner_filled`
dans `out/`. Rien n'est réservé en dry-run. Ensuite, éventuellement tester
`python make_invite.py` (fonctionne aussi sur un `result.json` en `dry_run`).

## Limite connue : captcha anti-robot

tennis.paris.fr affiche une **vérification de sécurité (captcha image)** juste
après le clic « Réserver », précisément pour bloquer les réservations
automatisées (constaté au calage : « nous bloquons les robots… », avec mention
« Blacklisté »). Dans ce cas le script s'arrête proprement
(`status=error`, raison `CaptchaRequired`, capture dans `out/`) et la routine
envoie le mail d'échec. Le contournement automatique du captcha est
volontairement exclu ; si le captcha est actif le jour J, la réservation doit
être faite à la main.

## Garde-fous

- Jamais d'autre créneau que la cible ; jamais de validation si un montant non
  nul en euros est affiché ; le mot de passe n'apparaît jamais dans les logs.
- `out/` (captures, dumps, résultats) et `.env` ne sont jamais committés.
