from flask import Flask,render_template
from flasgger import Swagger

from app.models import connect_to_ollama 
# from app.database.mongo_client import connect_to_mongodb 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def build_flask_endpoints(application):
    from app.api.endpoints import query_blueprint
    application.register_blueprint(query_blueprint)
swagger = Swagger(app) 

# check_mongodb  = connect_to_mongodb()
# if check_mongodb[0] == False:
#     print("\033[91m {}\033[00m".format(check_mongodb[1]))
#     print("\033[96m {}\033[00m".format(" - "*30))
check_ollama = connect_to_ollama()
if check_ollama[0] == False:
    print("\033[91m {}\033[00m".format(check_ollama[1]))
    print("\033[96m {}\033[00m".format(" - "*30))

build_flask_endpoints(app)