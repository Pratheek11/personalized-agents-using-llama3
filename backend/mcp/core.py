from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks.base import BaseCallbackHandler
from langchain.memory import ConversationBufferMemory
from mcp.tools import tools
from mcp.instructions.agentBehaviour import system_message
from typing import Any, Dict, List
import asyncio
import json
import re

class StreamingCallbackHandler(BaseCallbackHandler):
    """Enhanced callback handler for streaming responses with better formatting"""
    
    def __init__(self, queue):
        self.queue = queue
        self.current_tool = None
        self.tool_usage_count = {}
        self.final_answer_buffer = ""
        
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        """Send each token as it's generated"""
        self.queue.put_nowait({
            "type": "token",
            "content": token
        })
        
        # Buffer tokens for final answer processing
        self.final_answer_buffer += token
    
    def on_tool_start(self, serialized: Dict[str, Any], input_str: str, **kwargs) -> None:
        """Show when tool starts and track usage"""
        tool_name = serialized.get('name', 'Unknown')
        self.current_tool = tool_name
        
        # Track tool usage to prevent loops
        self.tool_usage_count[tool_name] = self.tool_usage_count.get(tool_name, 0) + 1
        
        self.queue.put_nowait({
            "type": "tool_start",
            "content": f"🔧 Using {tool_name}..."
        })
    
    def on_tool_end(self, output: str, **kwargs) -> None:
        """Show when tool completes"""
        self.queue.put_nowait({
            "type": "tool_end",
            "content": f"✅ {self.current_tool} completed"
        })
    
    def on_agent_finish(self, finish, **kwargs) -> None:
        """Process final answer with better formatting"""
        output = finish.return_values.get('output', '')
        
        # Clean up the output
        cleaned_output = self.clean_final_output(output)
        
        self.queue.put_nowait({
            "type": "final_response",
            "content": cleaned_output
        })
    
    def clean_final_output(self, output: str) -> str:
        """Clean and format the final output"""
        # Fix Unicode characters
        output = output.encode('utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')
        
        # Clean up extra whitespace
        output = re.sub(r'\n\s*\n', '\n\n', output)
        output = output.strip()
        
        return output

def create_streaming_agent(callback_handler):
    """Create agent with streaming support and better formatting"""
    
    # Add memory to prevent loops
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    llm = OllamaLLM(
        model="llama3",
        temperature=0.3,
        callbacks=[callback_handler],
        verbose=False  # Reduce verbosity to clean up output
    )
    
    # Enhanced system message
    enhanced_system_message = system_message + """
    OUTPUT FORMATTING RULES:
    1. Provide clean, well-formatted responses
    2. Use proper markdown formatting
    3. Don't include phrases like "Final Answer:" or "That's it!"
    4. Present information clearly and concisely
    5. Use emojis appropriately for visual appeal

    RESPONSE STRUCTURE:
    - Start directly with the requested information
    - Use headers and bullet points for clarity
    - End naturally without unnecessary closing phrases
    """
    
    return initialize_agent(
        tools,
        llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        memory=memory,
        max_iterations=5,
        early_stopping_method="generate",
        agent_kwargs={
            "system_message": enhanced_system_message
        }
    )