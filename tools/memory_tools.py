from tools.tool_registry import rregistry

@rregistry.register_tool()
class RememberFactTool:
    def __init__(self):
        self.name = "remember fact"
        self.description = (
            "Stores an important fact or user preference into long-term memory. "
            "Use this when the user shares personal info, preferences, or important context. "
            "Input format: 'key | value'  e.g. 'user_name | Siddhesh'"
        )
        self.memory = None  # injected by Agent after registration
    
    def run(self, query: str):
        try:
            if self.memory is None:
                return "Error: Memory not connected to RememberFactTool."
            if "|" not in query:
                return "Error: Input must be in format 'key | value'"
            key, value = query.split("|", 1)
            self.memory.remember(key.strip(), value.strip())
            return f"Got it! I've remembered that your {key.strip()} is {value.strip()}."
        except Exception as e:
            return f"Error storing memory: {str(e)}"