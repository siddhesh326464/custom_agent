from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class AgentState:
    """
    Represents the current execution state of the agent.
    """
    current_query: str = ""
    planned_actions: dict = field(default_factory=dict)
    response: str = ""
    def reset(self):
        """
        Reset state for a new user query.
        """
        self.current_query = ""
        self.planned_actions = {}
        self.response = ""
        
