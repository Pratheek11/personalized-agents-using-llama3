from langchain.agents import Tool
from mcp.agents.scheduleAgent.gmail import summarize_emails
from mcp.agents.scheduleAgent.gmeet import summarize_meetings
from mcp.agents.scheduleAgent.summarise import summarize_today

tools = [
    Tool(
        name="EmailAgent",
        func=summarize_emails,
        coroutine=summarize_emails,
        description=(
            "WHEN TO USE: User asks specifically about emails, Gmail, messages, or unread items.\n"
            "EXAMPLES: 'Check my emails', 'Any new messages?', 'Show unread emails'\n"
            "RETURNS: Summary of unread emails from yesterday.\n"
            "NOTE: Use this ONLY for email-specific queries, not general summaries."
        )
    ),
    Tool(
        name="CalendarAgent",
        func=summarize_meetings,
        coroutine=summarize_meetings,
        description=(
            "WHEN TO USE: User asks specifically about meetings, calendar, or today's schedule.\n"
            "EXAMPLES: 'What meetings do I have?', 'Show my calendar', 'Any meetings today?'\n"
            "RETURNS: List of Google Meet meetings scheduled for today.\n"
            "NOTE: Use this ONLY for calendar/meeting-specific queries, not general summaries."
        )
    ),
    Tool(
        name="DailySummaryAgent",
        func=summarize_today,
        coroutine=summarize_today,
        description=(
            "WHEN TO USE: User wants a complete daily overview or summary.\n"
            "EXAMPLES: 'Summarize today', 'What happened today?', 'Daily update', 'Give me today's summary'\n"
            "RETURNS: Combined summary of emails and calendar events.\n"
            "NOTE: This tool combines both email and calendar data - use for comprehensive summaries."
        )
    ),
]