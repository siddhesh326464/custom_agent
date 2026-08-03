from tools.tool_registry import rregistry

@rregistry.register_tool()
class ChatTool:
    def __init__(self):
        
        self.name = "llm" 
        self.description = "Use this tool to reply directly to the user for general conversation. Input must be your conversational response."
        
    def run(self, query: str) -> str:
        return query
