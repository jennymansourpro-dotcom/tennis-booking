#!/usr/bin/env python3
"""Génère l'invitation à partir de out/result.json :
  - out/invitation.ics   (fichier iCalendar)
  - out/gcal_link.txt    (lien Google Calendar pré-rempli)
  - out/email_body.txt   (corps du mail de confirmation)
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo

OUT_DIR = Path(__file__).resolve().parent / "out"


def main():
    result_path = OUT_DIR / "result.json"
    if not result_path.exists():
        print("out/result.json introuvable — lancer d'abord book_tennis.py", file=sys.stderr)
        return 1

    result = json.loads(result_path.read_text(encoding="utf-8"))
    if result.get("status") not in ("booked", "dry_run"):
        print(f"status={result.get('status')} — pas d'invitation à générer", file=sys.stderr)
        return 1

    start = datetime.fromisoformat(result["start_iso"])
    end = datetime.fromisoformat(result["end_iso"])
    site = result["site"]
    court = result["court"]
    partner = result["partner"]

    title = f"Tennis — {site} (court {court})"
    location = f"{site}, Paris {result['arrondissement']}e"
    description = (
        f"Réservation tennis.paris.fr\n"
        f"Court {court} — {site}\n"
        f"Partenaire : {partner}"
    )

    utc = ZoneInfo("UTC")
    fmt = "%Y%m%dT%H%M%SZ"
    start_utc = start.astimezone(utc).strftime(fmt)
    end_utc = end.astimezone(utc).strftime(fmt)
    stamp = datetime.now(utc).strftime(fmt)

    ics = "\r\n".join([
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//tennis-booking//book_tennis//FR",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "BEGIN:VEVENT",
        f"UID:tennis-{result['target_date']}-court{court}@tennis-booking",
        f"DTSTAMP:{stamp}",
        f"DTSTART:{start_utc}",
        f"DTEND:{end_utc}",
        f"SUMMARY:{title}",
        f"LOCATION:{location}",
        "DESCRIPTION:" + description.replace("\n", "\\n"),
        "END:VEVENT",
        "END:VCALENDAR",
        "",
    ])
    (OUT_DIR / "invitation.ics").write_text(ics, encoding="utf-8")

    gcal_link = (
        "https://calendar.google.com/calendar/render?action=TEMPLATE"
        f"&text={quote(title)}"
        f"&dates={start_utc}/{end_utc}"
        f"&location={quote(location)}"
        f"&details={quote(description)}"
    )
    (OUT_DIR / "gcal_link.txt").write_text(gcal_link + "\n", encoding="utf-8")

    date_fr = start.strftime("%d/%m/%Y")
    heure_fr = start.strftime("%Hh%M")
    email_body = (
        f"Bonjour,\n"
        f"\n"
        f"Le créneau de tennis est réservé ✅\n"
        f"\n"
        f"  • Date : {date_fr} de {heure_fr} à {end.strftime('%Hh%M')}\n"
        f"  • Lieu : {location}\n"
        f"  • Court : n°{court}\n"
        f"  • Partenaire : {partner}\n"
        f"\n"
        f"Ajouter au calendrier Google :\n{gcal_link}\n"
        f"\n"
        f"L'invitation .ics est jointe si votre client mail le permet.\n"
        f"\n"
        f"Bonne partie !\n"
    )
    (OUT_DIR / "email_body.txt").write_text(email_body, encoding="utf-8")

    print("invitation.ics, gcal_link.txt et email_body.txt générés dans out/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
