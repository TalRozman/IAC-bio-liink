import ollama 
from app.config import OLLAMA_URI

ollama_client = ollama.Client(host=OLLAMA_URI)

def connect_to_ollama() -> tuple[bool,str]:
    """
        connect to ollama service.
        \nparam: 
        \n\tNone
        \nreturns: 
        \n\ttuple: (status: bool,message: str)
    """
    try:
        models_list = ollama_client.list()
        status = create_model(models_list)
        if status[0] == False:
            return (False, status[1])
        return (True, "Connection and model creation completed successfully")
    except Exception as e:
        return (False, f"Error connecting to Ollama: {e}")
    

def create_model(model_list) -> tuple[bool,str]:
    """
        pulls all the required models and create a custom model based on llama3.2
        \nparam: 
        \n\tNone
        \nreturns: 
        \n\ttuple: (status: bool,message: str)
    """
    models = [model.model for model in model_list.models]
    if ("llama3.2:latest" in models) and ("myModel:latest" in models) :
            return (True, "all required models exist")
    
    try:
        ollama_client.pull("llama3.2")
        ollama_client.create(model='myModel', 
        from_="llama3.2", 
        system='''
            You are an expert medical triage and injury classification assistant.
            Your task is to analyze the provided information about an injury and assign it a specific "Injury Rank" based on a standardized scale.
        ''',
        parameters={"temperature" :0.2})

        return (True, "all models pulled and created successfully")
    except Exception as e:
        return (False, f"Error while pulling or creating ollama model: {e}")
