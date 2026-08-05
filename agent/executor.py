from tools.tool_registry import rregistry
from agent.state import AgentState

class Executor:
    def __init__(self):
        pass

    def execute(self, action_dict: dict, state: AgentState) -> dict:
        tool_name = action_dict.get("tool")
        query = action_dict.get("input")

        if not tool_name:
            state.response = "Tool name not specified"
            return {"error":"Tool name not specified"}   
        result = rregistry.execute_tool(tool_name, query)
        state.response = result
        return {"output": result}


        
        

    