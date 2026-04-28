from app.models import ollama_client
from app.rag.output_parser import output_parser_medical
from app.config import OLLAMA_SYSTEM_SETTINGS

def get_rag_chain_medical(prompt:str):
    """
        sends a query to the ollama service
        \nparam: 
        \n\tstr: prompt
        \nreturns: 
        \n\tRAG response: a parsed pydantic response 
    """
    response = ollama_client.generate(model="llama3.2",system=OLLAMA_SYSTEM_SETTINGS, prompt=prompt,options={"temperature": 0.0},format="json")
    parsed = output_parser_medical.parse(response.response)
    return parsed
