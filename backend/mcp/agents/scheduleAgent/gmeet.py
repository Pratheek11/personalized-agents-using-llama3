from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime

async def summarize_meetings(query: str = "") -> str:
    """Summarize today's meetings with proper formatting"""
    try:
        creds = Credentials.from_authorized_user_file("app/credentials/token.json")
        service = build("calendar", "v3", credentials=creds)

        # Get today's date range
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

        if not events:
            return "📅 **No meetings scheduled for today.**"

        # Filter for events with Google Meet links
        meet_events = []
        for event in events:
            has_meet_link = (
                event.get('conferenceData', {}).get('entryPoints') or
                'hangoutLink' in event
            )
            
            if has_meet_link:
                meet_events.append(event)

        if not meet_events:
            return "📅 **No Google Meet meetings scheduled for today.**"

        # Format the meetings
        formatted_meetings = f"📅 **{len(meet_events)} Google Meet Meeting(s) Today:**\n\n"
        
        for i, event in enumerate(meet_events, 1):
            title = event.get('summary', 'No Title')
            
            # Format time
            start_time = event['start'].get('dateTime')
            if start_time:
                # Parse and format the time
                start_dt = datetime.datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                # Convert to local time (you might want to adjust timezone)
                time_str = start_dt.strftime('%I:%M %p')
            else:
                time_str = 'All Day'
            
            # Get attendees count
            attendees = event.get('attendees', [])
            attendee_count = len(attendees) if attendees else 0
            
            formatted_meetings += f"**{i}. {title}**\n"
            formatted_meetings += f"   ⏰ Time: {time_str}\n"
            if attendee_count > 0:
                formatted_meetings += f"   👥 Attendees: {attendee_count}\n"
            formatted_meetings += f"   🔗 Google Meet link available\n\n"
        
        return formatted_meetings.strip()
        
    except Exception as e:
        return f"Error accessing calendar: {str(e)}"