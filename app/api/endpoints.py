import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from flasgger import swag_from
from flask import Blueprint,request

from app.api.swagger import query_endpoint
from app.rag.chain import get_rag_chain_medical
from app.rag.prompt_templates import build_prompt_medical


query_blueprint = Blueprint("query",__name__)


@query_blueprint.route('/query',methods=['POST'])
@swag_from(query_endpoint)
def query():
    """
    send query to LLM model
    """
    try:
        user_question = request.form.get("question")
    except Exception as e:
        return {
            'success': False,
            'message': f'Error with user question : {str(e)}',
        }, 500
    prompt = build_prompt_medical(user_question)
    answer = get_rag_chain_medical(prompt)
    response_dict = answer.model_dump()
    return {
        'success': True,
        'message': 'successfully answered the question',
        'data': response_dict
        }, 200