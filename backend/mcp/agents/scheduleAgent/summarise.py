from mcp.agents.scheduleAgent.gmail import summarize_emails
from mcp.agents.scheduleAgent.gmeet import summarize_meetings
import asyncio

async def summarize_today(_: str = "") -> str:
    """Generate a comprehensive daily summary with proper formatting"""
    try:
        # Get both summaries concurrently
        email_summary, calendar_summary = await asyncio.gather(
            summarize_emails(),
            summarize_meetings()
        )
        
        # Create formatted daily summary
        daily_summary = "# 📋 Daily Summary\n\n"
        
        # Add email section
        daily_summary += "## 📧 Email Summary\n"
        daily_summary += f"{email_summary}\n\n"
        
        # Add calendar section
        daily_summary += "## 📅 Calendar Summary\n"
        daily_summary += f"{calendar_summary}\n\n"
        
        return daily_summary
        
    except Exception as e:
        return f"Error generating daily summary: {str(e)}"