from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory
from llm.groqllm import GroqLLM
from agent.state import AgentState
from tools.tool_registry import rregistry
from thinking.query_expander import QueryExpander
from thinking.synthesizer import Synthesizer

class Agent:
    def __init__(self):
        self.planner = Planner(llm=GroqLLM())
        self.executor = Executor()
        self.memory = Memory()
        self.expander = QueryExpander(llm=GroqLLM())
        self.synthesizer = Synthesizer(llm=GroqLLM())
        remember_tool = rregistry.get_tool("remember fact")
        if remember_tool:
            remember_tool.memory = self.memory

    def run(self, query):
        current_state = AgentState()

        long_term_context = self.memory.recall(query=query, top_k=3)

        plan = self.planner.plan(
            query,
            state=current_state,
            memory=self.memory,
            long_term_context=long_term_context
        )
        self.executor.execute(plan, state=current_state)

        self.memory.add_session_memory(query, current_state.response)
        
        return current_state.response