from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from mcp.core import create_streaming_agent, StreamingCallbackHandler
import asyncio
import json

router = APIRouter(prefix="/mcp")

@router.post("/prompt")
async def stream_prompt(request: Request):
    body = await request.json()
    query = body.get("query", "")
    
    if not query:
        return {"error": "Query cannot be empty"}
    
    async def generate_stream():
        # Create queue for streaming messages
        stream_queue = asyncio.Queue()
        
        # Create callback handler
        callback_handler = StreamingCallbackHandler(stream_queue)
        
        # Create streaming agent
        streaming_agent = create_streaming_agent(callback_handler)
        
        # Process agent in background
        async def process_agent():
            try:
                result = await streaming_agent.ainvoke({"input": query})
                await stream_queue.put({
                    "type": "final_response",
                    "content": result["output"]
                })
            except Exception as e:
                await stream_queue.put({
                    "type": "error",
                    "content": str(e)
                })
            finally:
                await stream_queue.put({"type": "done"})
        
        # Start processing
        task = asyncio.create_task(process_agent())
        
        # Stream responses
        try:
            while True:
                # Get next message
                message = await stream_queue.get()
                
                if message["type"] == "done":
                    break
                
                # Send as Server-Sent Event
                yield f"data: {json.dumps(message)}\n\n"
                
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"
        finally:
            if not task.done():
                task.cancel()
    
    return StreamingResponse(
        generate_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )
