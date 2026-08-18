# Prompt de la routine — Réservation tennis du mercredi

Tu es la routine hebdomadaire de réservation de tennis. Lis `CLAUDE.md` pour le
contexte et les interdits. Exécute exactement ceci :

1. **Sans aucun délai ni étape préalable**, lance :

   ```bash
   python book_tennis.py
   ```

   Le script gère lui-même l'attente jusqu'à 08:00:00 heure de Paris et la
   recherche du créneau. Ne le lance qu'une seule fois ; laisse-le aller au bout.

2. Lis `out/result.json`.

3. **Si `status` = `booked`** :
   - Lance `python make_invite.py`.
   - Crée l'événement dans le calendrier via le **connecteur Google Calendar**
     (titre, lieu, début/fin repris de `result.json` / `out/invitation.ics`).
   - Envoie un mail via le **connecteur Gmail** à **jennymansour96@gmail.com**
     avec pour corps le contenu de `out/email_body.txt`, et joins
     `out/invitation.ics` si l'envoi de pièce jointe est possible.

4. **Si `status` = `not_found` ou `error`** :
   - Envoie un mail court via Gmail à **jennymansour96@gmail.com** : indique le
     `status`, la `reason` de `result.json`, et joins la capture la plus
     pertinente de `out/` (`99_error.png` s'il existe, sinon la dernière étape).
   - Ne tente **aucune** nouvelle réservation.

## Règles strictes

- **Aucune reprise après 08:15 heure de Paris.** Si à 08:15 la réservation n'est
  pas faite, on s'arrête et on envoie le mail d'échec. Ne relance pas le script.
- **Jamais un autre créneau** : ni autre heure, ni autre court, ni autre site,
  ni autre jour. Le créneau cible est fixé par les variables d'environnement.
- Ne valide jamais un écran affichant un montant non nul en euros.
- Si `reason` mentionne un captcha (`CaptchaRequired`) : n'essaie **jamais** de
  le résoudre ou de le contourner ; envoie le mail d'échec en précisant que la
  réservation doit être faite à la main avant que le créneau ne parte.
- N'expose jamais le mot de passe (logs, mails, commits).
- Ne committe ni ne pousse rien depuis la routine.
