from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from mcp.tools import tools
from mcp.instructions.agentBehaviour import system_message

llm = OllamaLLM(model="llama3")

agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    agent_kwargs={
        "system_message": system_message
    }
)