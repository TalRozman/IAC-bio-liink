import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import flask

from app.rag.chain import get_rag_chain_medical
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
        user_question = flask.request.data
    except Exception as e:
        return {
            'success': False,
            'message': f'Error with user question : {str(e)}',
        }, 500
    
    prompt = build_prompt_medical(user_question)

    schema = {
    "type": "object",
    "properties": {
        "Rank": { "type": "string" },
        "Justification": { "type": "string" },
        "Key_Medical_Indicators": { "type": "array", "items": {"type": "string"} }
    },
    "required": ["Rank", "Justification", "Key_Medical_Indicators"]
    }

    def generate():
        open_braces = 0
        for chunk in ollama_client.generate(model="llama3.2:1b",system=OLLAMA_SYSTEM_SETTINGS, prompt=prompt,format=schema, options={
            "temperature": 0.0,
            "num_predict": 75,
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

    # answer = get_rag_chain_medical(prompt)
    # response_dict = answer.model_dump()
    # return {
    #     'success': True,
    #     'message': 'successfully answered the question',
    #     'data': response_dict
    #     }, 200