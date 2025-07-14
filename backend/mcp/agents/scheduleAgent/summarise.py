from mcp.agents.scheduleAgent.gmail import summarize_emails
from mcp.agents.scheduleAgent.gmeet import summarize_meetings
import asyncio

async def summarize_today(_: str = "") -> str:
    email_summary, calendar_summary = await asyncio.gather(
        summarize_emails(),
        summarize_meetings()
    )
    return (
        f"📬 **Email Summary:**\n{email_summary}\n\n"
        f"📅 **Calendar Summary:**\n{calendar_summary}"
    )
