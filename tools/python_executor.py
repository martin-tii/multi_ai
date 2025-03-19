from langchain.tools import Tool
from executor import safe_python_executor

python_execution_tool = Tool(
    name="Python Executor",
    func=safe_python_executor,
    description="Executes Python code and returns the result."
)
