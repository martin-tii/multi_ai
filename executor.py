import builtins

def safe_python_executor(code: str):
    """
    Executes Python code safely with restricted builtins.
    """
    try:
        safe_globals = {"__builtins__": {"print": builtins.print, "range": range}}
        exec(code, safe_globals)
        return "Execution completed successfully."
    except Exception as e:
        return str(e)
