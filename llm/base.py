from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class BaseLLM(ABC):
    def __init__(self,model_name: str,temperature: float = 0.0,max_tokens: int = 1024):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

    @abstractmethod
    def generate(self, user_query: str) -> str:
        pass
        
        

    