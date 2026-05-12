import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import flask

from app.rag.prompt_templates import build_prompt_medical

from app.models import ollama_client
from app.config import OLLAMA_SYSTEM_SETTINGS


query_blueprint = flask.Blueprint("query",__name__)

@query_blueprint.route('/query',methods=['POST'])
def query():
    """
    send query to LLM model
    """
    try:
        user_question = flask.request.data.decode('utf-8')
    except Exception as e:
        return {
            'success': False,
            'message': f'Error with user question : {str(e)}',
        }, 500
    
    prompt = build_prompt_medical(user_question)

    schema = {
        "type": "object",
        "properties": {
            "Primary_Severe_Injury": { "type": "string" },
            "Rank": { 
                "type": "string",
                "enum": ["LIGHT", "MODERATE", "SERIOUS", "SEVERE", "CRITICAL", "UNSURVIVEABLE"] # <--- THIS IS THE MAGIC FIX
            },
            "Justification": { "type": "string" },
            "Key_Medical_Indicators": { "type": "array", "items": {"type": "string"} }
        },
        "required": ["Primary_Severe_Injury", "Rank", "Justification", "Key_Medical_Indicators"]
    }

    def generate():
        open_braces = 0
        for chunk in ollama_client.generate(model="llama3.2:1b",system=OLLAMA_SYSTEM_SETTINGS, prompt=prompt,format=schema, options={
            "temperature": 0.0,
            "num_predict": 250,
            "top_k": 1,
            "top_p": 1.0,
            "num_ctx": 1024,
            "use_mmap": True,
            "stop": ["STOP_GENERATION", "}\n{", "}\n\n{"]
            },keep_alive=-1,stream=True):
            text = chunk['response']
            open_braces += text.count('{')
            open_braces -= text.count('}')
            
            if '{' in text:
                has_started = True
                
            yield text.encode('utf-8')

            if has_started and open_braces == 0:
                break
    return flask.Response(generate(), mimetype="text/plain",direct_passthrough=True)