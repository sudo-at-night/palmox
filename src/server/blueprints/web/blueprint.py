from flask import Blueprint, request, make_response
from werkzeug.exceptions import HTTPException, Unauthorized
from db.postgres import db_session
from models.user import User

web_blueprint = Blueprint("web", __name__)


@web_blueprint.post("/login")
def login():
    if (
        not request.json
        or "email" not in request.json
        or "password" not in request.json
    ):
        raise Unauthorized("Wrong credentials passed")

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


@web_blueprint.errorhandler(HTTPException)
def handle_request_error(err):
    response = make_response()
    response.status_code = err.code

    return response
