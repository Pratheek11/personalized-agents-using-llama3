from mcp.agent_registry import get_agents_for_intent
from mcp.llm_router import summarize_text, generate_text
from mcp.instructions.breif import llm_prompt, email_prompt, meeting_prompt

class MCP:
    def __init__(self):
        pass

    async def handle(self, user_prompt: str):
        instructions = []
        instructions.append(llm_prompt)
        # Step 1: Decide how to handle the prompt
        # Could be agent, LLM-only, or hybrid
        if "email" in user_prompt.lower():
            intent = "summarize_gmail"
            instructions.append(email_prompt)
        elif "meeting" in user_prompt.lower():
            intent = "summarize_gmeet"
            instructions.append(meeting_prompt)
        elif "today" in user_prompt.lower() and "summarize" in user_prompt.lower():
            intent = "summarize_today"
            instructions.append(email_prompt)
            instructions.append(meeting_prompt)
        else:
            # fallback to LLM only if no match
            return {
                "answer": await generate_text(user_prompt)
            }

        # Step 2: Get matching agents
        agents = get_agents_for_intent(intent)
        if not agents:
            return {"error": f"No agents found for intent: {intent}"}

        # Step 3: Collect results from agents
        results = []
        for agent in agents:
            output = await agent()
            results.append(output)

        # Step 4: Summarize combined output
        merged = " ".join(results)
        final_summary = await summarize_text(merged, instructions)

        return {
            "answer": final_summary,
        }
