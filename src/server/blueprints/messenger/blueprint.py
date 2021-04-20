from flask import Blueprint, render_template, request
from flask_graphql import GraphQLView
from dotenv import dotenv_values
from .gql import schema

config = dotenv_values(".env")
is_playground_enabled = config["GRAPHQL_ENABLE_PLAYGROUND"] == 'true'

messenger_blueprint = Blueprint("messenger", __name__)

messenger_blueprint.add_url_rule(
    "/gql", view_func=GraphQLView.as_view("graphql", schema=schema)
)


if is_playground_enabled:

    @messenger_blueprint.route("/gql/docs")
    def gql_playground():
        return render_template("graphql-playground.html")
