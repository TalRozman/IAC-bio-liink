import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI',"mongodb://localhost:27017")
OLLAMA_URI = os.environ.get("OLLAMA_URI","localhost:11434")
