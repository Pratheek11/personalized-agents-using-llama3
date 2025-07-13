from langchain.agents import Tool
from mcp.agents.scheduleAgent.gmail import summarize_emails
from mcp.agents.scheduleAgent.gmeet import summarize_meetings
from mcp.agents.scheduleAgent.summarise import summarize_today

tools = [
    
    Tool(name="EmailAgent", 
        func=summarize_emails, 
        description="Summarizes user emails"
        "Input should be a plain text string. "
        "Always return a valid JSON object with double quotes only."
    ),

    Tool(
        name="CalendarAgent",
        func=summarize_meetings, 
        description="Use this tool to summarize today's calendar events. "
        "Input should be a plain text string. "
        "Always return a valid JSON object with double quotes only."
    ),

    Tool(
        name="DailySummaryAgent",
        func=summarize_today,
        description="Use this to summarize both emails and calendar for today when asked like Summarize my day/Summarize today events etc."
        "Input should be a plain text string. "
        "Returns a markdown-formatted response."
    )
]
