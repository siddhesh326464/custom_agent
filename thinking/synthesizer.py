from llm.groqllm import GroqLLM
from thinking.prompts import SYNTHESIZER_PROMPT



class Synthesizer:
    def __init__(self):
        self.synthesizer_llm = GroqLLM()

    def synthesize(self,query:str,aggregated_results: str):
        prompt = SYNTHESIZER_PROMPT.format(original_query=query,aggregated_results=aggregated_results)
        final_prompt = self.synthesizer_llm.generate(prompt)
        return final_prompt


