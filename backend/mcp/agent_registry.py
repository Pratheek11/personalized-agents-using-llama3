from typing import List, Callable
from mcp.agents.scheduleAgent.gmail import summarize_emails
from mcp.agents.scheduleAgent.gmeet import summarize_meetings

def get_agents_for_intent(intent: str) -> List[Callable]:
    registry = {
        "summarize_today": [summarize_meetings, summarize_emails],
        "summarize_gmeet": [summarize_meetings],
        "summarize_gmail": [summarize_emails]
    }
    return registry.get(intent, [])
