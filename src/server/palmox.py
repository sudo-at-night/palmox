from flask import Flask
from blueprints.web import web_blueprint

app = Flask(__name__)
app.register_blueprint(web_blueprint)
