from flask import Flask
from db.postgres import init_db, db_session
from blueprints.messenger import messenger_blueprint
from blueprints.web import web_blueprint

app = Flask(__name__)
app.register_blueprint(messenger_blueprint)
app.register_blueprint(web_blueprint)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()
