import json
from llm.groqllm import GroqLLM
from agent.state import AgentState
from agent.prompts import PLANNER_PROMPT
from tools.tool_registry import rregistry


class Planner:
    def __init__(self,llm:GroqLLM):
        self.planner_llm = llm

    def plan(self, user_query, state: AgentState, memory):
        state.current_query = user_query
        
        available_tools = rregistry.get_tool_descriptions_for_llm()
        chat_history = memory.get_formatted_history()
        
        final_prompt = PLANNER_PROMPT.format(
            tools=available_tools,
            history=chat_history,
            query=state.current_query
        )
        
        response = self.planner_llm.generate(final_prompt)
        try:
            clean_text = response.replace("```json", "").replace("```", "").strip()
            action_dict = json.loads(clean_text)
            state.planned_actions = action_dict
            return action_dict

        except json.JSONDecodeError:
            return {"tool": "llm", "input": response}
