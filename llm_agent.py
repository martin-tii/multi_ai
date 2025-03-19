from langchain_experimental.tools import PythonREPLTool
from langchain.agents import initialize_agent, AgentType
from langchain_ollama import OllamaLLM
from tools.python_executor import python_execution_tool
from tools.function_tools import custom_functions

# Initialize Ollama LLM
llm = OllamaLLM(model="phi4:latest")

# Define available tools
tools = [PythonREPLTool(), python_execution_tool] + custom_functions

# Use ConversationalAgent (better for tools with structured inputs)
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    #agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,  # Changed from ZERO_SHOT
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
