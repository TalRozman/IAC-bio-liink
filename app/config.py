import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI',"mongodb://localhost:27017")
OLLAMA_URI = os.environ.get("OLLAMA_URI","localhost:11434")

OLLAMA_SYSTEM_SETTINGS ='''
You are an expert medical triage and injury classification assistant. Your task is to analyze the provided information about an injury and assign it a specific "Injury Rank" based on a standardized scale. 
'''