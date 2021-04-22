from flask import Blueprint
from db.postgres import db_session
from models.project import PostgresProject
from models.feature_flag import PostgresFeatureFlag

web_blueprint = Blueprint("web", __name__)


@web_blueprint.route("/ping")
def ping():
    return "pong"
