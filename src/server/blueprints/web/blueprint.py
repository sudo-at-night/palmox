from flask import Blueprint, request, make_response
from werkzeug.exceptions import Conflict, HTTPException, Unauthorized, BadRequest
from jsonschema import validate, FormatChecker, ValidationError
from db.postgres import db_session
from models.user import User
from .forms import login_schema, register_schema

web_blueprint = Blueprint("web", __name__)


@web_blueprint.post("/login")
def login():
    try:
        validate(
            instance=request.json, schema=login_schema, format_checker=FormatChecker()
        )
    except ValidationError:
        raise BadRequest("Bad request")

    response = make_response()
    response.status_code = 204

    email: str = request.json["email"]
    password: str = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        raise Unauthorized(f"User with email '{email}'' not found")

    if not user.check_password(password):
        raise Unauthorized(f"Wrong credentials passed for user with email '{email}'")

    user.refresh_auth_token()
    db_session.commit()

    response.set_cookie("FSESSIONID", user.auth_token, httponly=True)

    return response


@web_blueprint.get("/logout")
def logout():
    response = make_response()
    response.status_code = 204

    auth_cookie = request.cookies.get("FSESSIONID")

    if auth_cookie is None:
        return response

    user = User.get_by_auth_token(auth_cookie)

    if user is not None:
        user.invalidate_auth_token()
        db_session.commit()

    response.delete_cookie("FSESSIONID", httponly=True)

    return response


@web_blueprint.post("/register")
def register():
    try:
        validate(
            instance=request.json,
            schema=register_schema,
            format_checker=FormatChecker(),
        )
    except ValidationError:
        raise BadRequest("Bad request")

    email: str = request.json["email"]
    password: str = request.json["password"]

    user = User.query.filter_by(email=email).first()
    if user is not None:
        raise Conflict(f"User with email '{email}' already exists in the database")

    new_user = User(email=email, password=password)
    db_session.add(new_user)
    db_session.commit()

    response = make_response()
    response.status_code = 201

    return response


@web_blueprint.errorhandler(HTTPException)
def handle_request_error(err):
    response = make_response()
    response.status_code = err.code

    return response
