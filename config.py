import os
from dotenv import load_dotenv
load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "llama3-8b-8192")
API_KEY = os.getenv("API_KEY", "your-default-key-here")
BASE_URL = os.getenv("BASE_URL", "https://api.groq.com/openai/v1")
