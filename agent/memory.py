

class Memory:
    def __init__(self):
        self.history = []

    def add_session_memory(self, user_input, agent_response):
        self.history.append({
            "user_input": user_input,
            "agent_response": agent_response
        })

    def get_formatted_history(self) -> str:
        if not self.history:
            return "No previous conversation history."
        
        formatted = []
        for entry in self.history[-10:]:
            formatted.append(f"User: {entry['user_input']}")
            formatted.append(f"Agent: {entry['agent_response']}")
        return "\n".join(formatted)