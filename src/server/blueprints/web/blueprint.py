from flask import Blueprint, request, make_response
from werkzeug.exceptions import HTTPException, Unauthorized
from models.user import User

web_blueprint = Blueprint("web", __name__)


@web_blueprint.post("/login")
def login():
    if "email" not in request.json or "password" not in request.json:
        raise Unauthorized(f"Wrong credentials passed")

    response = make_response()

    email: str = request.json["email"]
    password: str = request.json["password"]

    user: User = User.query.filter_by(email=email).first()

    if user is None:
        raise Unauthorized(f"User with email '{email}'' not found")

    if not user.check_password(password):
        raise Unauthorized(f"Wrong credentials passed for user with email '{email}'")

    user.refresh_auth_token()
    response.set_cookie("FSESSIONID", user.auth_token, httponly=True)

    response.status_code = 204
    return response


@web_blueprint.get("/logout")
def logout():
    response = make_response()

    response.delete_cookie("FSESSIONID", httponly=True)
    response.status_code = 204

    return response


@web_blueprint.errorhandler(HTTPException)
def handle_request_error(err):
    response = make_response()
    response.status_code = err.code

    return response
