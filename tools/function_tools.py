from langchain.tools import StructuredTool

# Define functions with explicit single string input
def get_temperature(query: str) -> str:
    """Returns the current temperature. Query parameter is ignored."""
    return "Current temperature is 25°C"

def fetch_data(query: str) -> str:
    """Fetches data from an API. Query parameter is ignored."""
    return "Fetching data from an API..."

# Register tools with explicit input parameters
custom_functions = [
    StructuredTool.from_function(get_temperature),
    StructuredTool.from_function(fetch_data)
]
