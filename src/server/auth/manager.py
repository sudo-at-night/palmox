from flask_login import LoginManager
from models.user import User

login_manager = LoginManager()


@login_manager.request_loader
def load_user(request):
    token = request.cookies.get("FSESSIONID")
    if token:
        user = User.get_by_auth_token(token)
        if user:
            return user

    return None