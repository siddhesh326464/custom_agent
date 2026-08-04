from agent.long_term_memory import LongTermMemory

class Memory:
    def __init__(self):
        self.history = []
        self.long_term_memory = LongTermMemory(
            url="https://7025458b-50eb-4bff-8e15-38b4449c1b59.us-west-1-0.aws.cloud.qdrant.io",
            api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6MTBmYzYyZjUtZjc5OC00ZjViLTkwMWMtNDM3ZGI0YzA4ZGE1In0.3Zh8U4EZg7Ozte5SMwGRqRpAEwiRpj9w2cydkmXQx5g"
        )

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

    def remember(self,key:str,value:str):
        self.long_term_memory.add_long_term_memory(key,value)

    def recall(self,query:str,top_k:int=5) -> str:
        return self.long_term_memory.get_all_formatted(query,top_k)