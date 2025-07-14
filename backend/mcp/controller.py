from fastapi import APIRouter, Request
from mcp.core import agent  # assumes this is the compiled LangGraph or LangChain agent

router = APIRouter(prefix="/mcp")

@router.post("/prompt")
async def handle_prompt(request: Request):
    body = await request.json()
    query = body.get("query", "")
    if not query:
        return {"error": "Query cannot be empty"}
    
    try:
        result = await agent.ainvoke({"input": query})
        return {"response": result["output"]}
    except Exception as e:
        print(f"Error processing query: {e}")
        return {"error": str(e)}
