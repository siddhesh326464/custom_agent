import json
import os
from llm.groqllm import GroqLLM
from agent.state import AgentState
from agent.prompts import PLANNER_PROMPT
from tools.tool_registry import rregistry

# Path to the optimized planner saved by RL/optimize.py
OPTIMIZED_PLANNER_PATH = os.path.join(
    os.path.dirname(__file__), "..", "RL", "optimized_planner.json"
)


def _load_few_shot_demos() -> str:
    """Load bootstrapped few-shot demos from optimized_planner.json if it exists."""
    path = os.path.abspath(OPTIMIZED_PLANNER_PATH)
    if not os.path.exists(path):
        return ""
    try:
        with open(path, "r") as f:
            data = json.load(f)
        demos = data.get("predict", {}).get("demos", [])
        if not demos:
            return ""
        lines = ["\n--- Few-Shot Examples (auto-loaded from RL optimization) ---"]
        for i, demo in enumerate(demos, 1):
            lines.append(f"\nExample {i}:")
            lines.append(f"  Query: {demo.get('query', '')}")
            lines.append(f"  Tool:  {demo.get('tool', '')}")
            lines.append(f"  Input: {demo.get('input', '')}")
        lines.append("--- End of Examples ---\n")
        return "\n".join(lines)
    except Exception:
        return ""


class Planner:
    def __init__(self, llm: GroqLLM):
        self.planner_llm = llm
        self.few_shot_demos = _load_few_shot_demos()
        if self.few_shot_demos:
            print("[Planner] Loaded optimized few-shot demos from RL/optimized_planner.json")
        else:
            print("[Planner] No optimized planner found, using base prompt.")

    def plan(self, user_query, state: AgentState, memory, long_term_context: str = ""):
        state.current_query = user_query

        available_tools = rregistry.get_tool_descriptions_for_llm()
        chat_history = memory.get_formatted_history()

        final_prompt = PLANNER_PROMPT.format(
            tools=available_tools,
            history=chat_history,
            query=state.current_query,
            cwd=os.getcwd(),
            home=os.path.expanduser("~"),
            long_term_memory=long_term_context
        )

        if self.few_shot_demos:
            final_prompt = final_prompt.replace(
                "User Query:", self.few_shot_demos + "User Query:"
            )

        response = self.planner_llm.generate(final_prompt)
        try:
            clean_text = response.replace("```json", "").replace("```", "").strip()
            action_dict = json.loads(clean_text)
            state.planned_actions = action_dict
            return action_dict

        except Exception as e:
            print(e)
            return {"tool": "llm", "input": response}
