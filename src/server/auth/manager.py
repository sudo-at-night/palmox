from flask_login import LoginManager
from models.user import PostgresUser

login_manager = LoginManager()


@login_manager.request_loader
def load_user(request):
    token = request.headers.get("Authorization")
    if token:
        token = token.replace("Bearer ", "", 1)

        user = PostgresUser.get_by_auth_token(token)
        if user:
            return user

    return None