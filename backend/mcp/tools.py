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
            "Use this tool **only** if the user specifically asks about:\n"
            "- unread emails\n"
            "- Gmail messages\n"
            "- messages received\n\n"
            "❌ Do not use this for greetings, general questions, or daily summaries.\n"
            "✅ Return a clean **Markdown** summary of unread emails."
        )
    ),
    Tool(
        name="CalendarAgent",
        func=summarize_meetings,
        coroutine=summarize_meetings,
        description=(
            "Use this tool **only** if the user specifically asks about:\n"
            "- today's meetings\n"
            "- today's calendar schedule\n"
            "- upcoming events today\n\n"
            "❌ Do not use this for greetings or general summaries.\n"
            "✅ Respond in clear **Markdown** format."
        )
    ),
    Tool(
        name="DailySummaryAgent",
        func=summarize_today,
        coroutine=summarize_today,
        description=(
            "Use this tool only if the user wants a full summary of the day, such as:\n"
            "- 'What happened today?'\n"
            "- 'Give me a daily update'\n"
            "- 'Summarize today's emails and calendar'\n\n"
            "✅ Combine email + calendar summaries into a single **Markdown** response."
        )
    ),
]
