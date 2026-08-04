import dspy
import os
from dotenv import load_dotenv

load_dotenv()

lm = dspy.LM(
    model=os.getenv("DSPY_MODEL_NAME"),   # groq/llama-3.3-70b-versatile
    api_key=os.getenv("GROQ_API_KEY"),    # LiteLLM reads this for Groq
)

dspy.configure(lm=lm)