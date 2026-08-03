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
        plan = self.planner.plan(query, state=current_state, memory=self.memory)
        self.executor.execute(plan, state=current_state)
        
        self.memory.add_session_memory(query, current_state.response)
        
        return current_state.response