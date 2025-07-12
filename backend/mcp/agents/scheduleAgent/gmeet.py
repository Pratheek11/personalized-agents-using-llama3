from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime

async def summarize_meetings():
    creds = Credentials.from_authorized_user_file("app/credentials/token.json")
    service = build("calendar", "v3", credentials=creds)

    now = datetime.datetime.utcnow()
    start = now.replace(hour=0, minute=0, second=0).isoformat() + 'Z'
    end = now.replace(hour=23, minute=59, second=59).isoformat() + 'Z'

    events = service.events().list(
        calendarId='primary',
        timeMin=start,
        timeMax=end,
        singleEvents=True,
        orderBy='startTime'
    ).execute().get('items', [])

    # Filter for events with Google Meet links
    meet_events = [
        e for e in events
        if e.get('conferenceData', {}).get('entryPoints')
        or ('hangoutLink' in e)
    ]

    text = "\n".join([
        f"{e['start'].get('dateTime', 'all-day')} - {e.get('summary', 'No title')}"
        for e in meet_events
    ])

    return text if text else 'No Google Meet meetings found.'