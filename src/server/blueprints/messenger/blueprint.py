from flask import Blueprint, render_template, request
from flask_graphql import GraphQLView
from .gql import schema


messenger_blueprint = Blueprint("messenger", __name__)


messenger_blueprint.add_url_rule(
    "/gql", view_func=GraphQLView.as_view("graphql", schema=schema)
)


@messenger_blueprint.route("/gql/docs")
def gql_playground():
    return render_template("graphql-playground.html")
