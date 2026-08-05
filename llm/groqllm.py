import os
from llm.base import BaseLLM
from openai import OpenAI
import config

class GroqLLM(BaseLLM):
    def __init__(self, model_name: str = config.MODEL_NAME, temperature: float = 0.0, max_tokens: int = 1000):
        super().__init__(model_name, temperature, max_tokens)
        self.client = OpenAI(
            api_key=config.API_KEY,
            base_url=config.BASE_URL   
        )

    def generate(self,user_query:str):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": user_query}],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content
