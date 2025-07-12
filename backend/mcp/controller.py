from fastapi import APIRouter, Request
from mcp.core import MCP

mcp = MCP()

router = APIRouter(prefix="/mcp")

@router.post("/prompt")
async def handle_prompt(request: Request):
    body = await request.json()
    query = body.get("query", "")
    try:
        if not query:
            return {"error": "Query cannot be empty"}
        return await mcp.handle(query)
    except Exception as e:
        return {"error": f"{str(e)}"}
    