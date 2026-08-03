import json
from llm.groqllm import GroqLLM
from agent.state import AgentState
from agent.prompts import PLANNER_PROMPT


class Planner:
    def __init__(self,llm:GroqLLM):
        self.planner_llm = llm

    def plan(self,user_query,state:AgentState):
        state.current_query = user_query
        query = state.current_query
        final_prompt = PLANNER_PROMPT.format(
            query=query,
        )
        response = self.planner_llm.generate(final_prompt)
        try:
            clean_text = response.replace("```json", "").replace("```", "").strip()
            action_dict = json.loads(clean_text)
            state.planned_actions = action_dict
            return action_dict

        except json.JSONDecodeError:
            return {"tool": "llm", "input": response_text}
        
        


