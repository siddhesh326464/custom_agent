import json
from llm.groqllm import GroqLLM
from .prompts import EXPANDER_PROMPT

class QueryExpander:
    def __init__(self):
        self.expander_llm = GroqLLM()

    def expand_query(self,query:str):
        prompt = EXPANDER_PROMPT.format(original_query=query)
        final_prompt = self.expander_llm.generate(prompt)
        sub_queries = json.loads(final_prompt)
        return sub_queries
