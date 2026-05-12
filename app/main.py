from flask import Flask,render_template
from app.models import connect_to_ollama 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def build_flask_endpoints(application):
    from app.api.endpoints import query_blueprint
    application.register_blueprint(query_blueprint)

check_ollama = connect_to_ollama()
if check_ollama[0] == False:
    print("\033[91m {}\033[00m".format(check_ollama[1]))
    print("\033[96m {}\033[00m".format(" - "*30))

build_flask_endpoints(app)