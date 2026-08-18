# Contexte agent — Routine de réservation tennis

Ce repo automatise la réservation d'un créneau de tennis fixe sur tennis.paris.fr.

## Cible (fixe, ne jamais dévier)

- **Site** : Tennis Edouard Pailleron, 19ème arrondissement
- **Créneau** : mercredi 19h–20h, **court 2** uniquement
- **Partenaire** : Mehdi Kellal (par défaut, surchargeable par env)

Tout est piloté par variables d'environnement (voir README.md). Aucun identifiant
n'est en dur dans le code.

## Règle des 8h

Les réservations ouvrent à **08:00:00 heure de Paris**. La routine se lance le
**jeudi à 07:52 heure de Paris** pour viser le mercredi suivant (prochain mercredi
strictement après le jour du lancement). `book_tennis.py` attend activement
l'ouverture (maintien de session par reload/60 s, puis rafale de reloads toutes
les 1,5 s) et abandonne après `TENNIS_DEADLINE_MINUTES` (6 min par défaut) ;
le script gère lui-même l'attente précise, la routine ne doit rien retarder.

## Fichiers

- `book_tennis.py` — réservation. Écrit `out/result.json`
  (`booked | dry_run | not_found | error`) + captures/dumps à chaque étape.
- `make_invite.py` — à partir de `result.json`, produit `out/invitation.ics`,
  `out/gcal_link.txt` et `out/email_body.txt`.
- `ROUTINE_PROMPT.md` — prompt exact de la routine planifiée.

## Limite connue : captcha anti-robot

Constaté au calage du 18/08/2026 : après le clic « Réserver », tennis.paris.fr
affiche une **vérification de sécurité (captcha image)** avec le message « nous
bloquons les robots qui pourraient agir à votre place » (et, lors du test, une
mention « vous avez été Blacklisté »). Le script détecte cette page
(`CaptchaRequired`) et échoue proprement avec `status=error` + capture d'écran.
**Ne jamais tenter de contourner ou de résoudre automatiquement ce captcha** —
c'est une protection explicite du site contre les réservations automatisées.
Si le captcha apparaît, la routine envoie le mail d'échec et s'arrête ; la
réservation doit alors être faite à la main.

## Interdits absolus

1. **Ne jamais réserver un autre créneau** (autre heure, autre court, autre site,
   autre jour). Si le créneau cible n'est pas disponible → `not_found`, on s'arrête.
2. **Ne jamais valider si un montant non nul en euros est affiché.** Le script
   refuse déjà ; ne pas contourner cette vérification.
3. **Ne jamais exposer le mot de passe** (`PARIS_TENNIS_PASSWORD`) — ni dans les
   logs, ni dans un mail, ni dans un commit, ni dans une capture commentée.
3bis. **Ne jamais contourner le captcha anti-robot** (résolution automatique,
   OCR, service tiers, rejeu de session…). Échec propre + mail, rien d'autre.
4. **Ne jamais committer** `out/`, `.env`, ni aucun fichier contenant des
   identifiants. Le repo est en lecture pendant la routine : ne pas committer
   ni pousser depuis la routine.

## Modes de test

- `DRY_RUN=1` : s'arrête juste avant la validation finale (status `dry_run`).
- `SKIP_WAIT=1` : saute l'attente de 08:00 (pour le calage des sélecteurs).
- Test complet à blanc : `DRY_RUN=1 SKIP_WAIT=1 python book_tennis.py`.
