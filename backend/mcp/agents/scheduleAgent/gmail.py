from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime
import re
import html

async def summarize_emails(query: str = "") -> str:
    """Summarize unread emails with proper formatting"""
    try:
        creds = Credentials.from_authorized_user_file("app/credentials/token.json")
        service = build("gmail", "v1", credentials=creds)

        # Calculate yesterday's date range
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        after = yesterday.strftime("%Y/%m/%d")
        before = today.strftime("%Y/%m/%d")

        # Gmail query: unread and after yesterday
        gmail_query = f"is:unread after:{after}"

        msgs = service.users().messages().list(userId='me', q=gmail_query).execute().get('messages', [])

        if not msgs:
            return "No unread emails from yesterday."

        email_summaries = []
        
        for i, msg in enumerate(msgs[:10]):  # Limit to 10 emails to avoid too much content
            try:
                data = service.users().messages().get(userId='me', id=msg['id'], format="full").execute()
                
                # Extract headers
                headers = data.get('payload', {}).get('headers', [])
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
                sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
                
                # Clean up sender (extract just name/email)
                sender_match = re.search(r'([^<]+)<([^>]+)>', sender)
                if sender_match:
                    sender = sender_match.group(1).strip()
                elif '<' in sender:
                    sender = sender.split('<')[0].strip()
                
                # Get snippet and clean it
                snippet = data.get('snippet', '')
                snippet = html.unescape(snippet)  # Decode HTML entities
                snippet = re.sub(r'\s+', ' ', snippet)  # Normalize whitespace
                
                # Limit snippet length
                if len(snippet) > 150:
                    snippet = snippet[:150] + "..."
                
                email_summaries.append({
                    'sender': sender,
                    'subject': subject,
                    'snippet': snippet
                })
                
            except Exception as e:
                continue  # Skip problematic emails
        
        if not email_summaries:
            return "No readable unread emails from yesterday."
        
        # Format the summary
        formatted_summary = f"📧 **{len(email_summaries)} Unread Email(s):**\n\n"
        
        for i, email in enumerate(email_summaries, 1):
            formatted_summary += f"**{i}. {email['subject']}**\n"
            formatted_summary += f"   From: {email['sender']}\n"
            formatted_summary += f"   Preview: {email['snippet']}\n\n"
        
        return formatted_summary.strip()
        
    except Exception as e:
        return f"Error accessing emails: {str(e)}"