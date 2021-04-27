from flask import Flask
from dotenv import dotenv_values
from db.postgres import init_db, db_session
from cache.redis import cache
from auth.manager import login_manager
from blueprints.exposable import exposable_blueprint
from blueprints.web import web_blueprint

config = dotenv_values(".env")

app = Flask(__name__)
app.register_blueprint(exposable_blueprint)
app.register_blueprint(web_blueprint)
app.secret_key = config["FLASK_SECRET_KEY"]
login_manager.init_app(app)
cache.init_app(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()
