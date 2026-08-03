from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory
from llm.groqllm import GroqLLM
from agent.state import AgentState

class Agent:
    def __init__(self):
        self.planner = Planner(llm=GroqLLM())
        self.executor = Executor()
        self.memory = Memory()

    def run(self,query):
        current_state = AgentState()
        plan = self.planner.plan(query,state=current_state)
        self.executor.execute(plan, state=current_state)
        return current_state.response