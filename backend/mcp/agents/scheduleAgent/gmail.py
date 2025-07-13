from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime

def summarize_emails(query: str = "") -> str:
    creds = Credentials.from_authorized_user_file("app/credentials/token.json")
    service = build("gmail", "v1", credentials=creds)

    # Calculate yesterday's date range
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    after = yesterday.strftime("%Y/%m/%d")
    before = today.strftime("%Y/%m/%d")

    # Gmail query: unread and after yesterday
    query = f"is:unread after:{after}"

    msgs = service.users().messages().list(userId='me', q=query).execute().get('messages', [])

    full_text = ""
    for msg in msgs:
        data = service.users().messages().get(userId='me', id=msg['id'], format="full").execute()
        full_text += data.get('snippet', '') + "\n---\n"

    return full_text if full_text else 'No unread emails from yesterday.'