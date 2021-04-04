from flask import Flask
from blueprints.messenger import messenger_blueprint
from blueprints.web import web_blueprint

app = Flask(__name__)
app.register_blueprint(messenger_blueprint)
app.register_blueprint(web_blueprint)
