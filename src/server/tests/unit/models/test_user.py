from datetime import datetime, timedelta
from models.user import User


def test_can_refresh_auth_token():
    """
    User's auth token can be refreshed.
    """
    user = User(email="test@mail.com", password="testme")

    assert user.auth_token is None
    assert user.auth_token_expiration is None

    user.refresh_auth_token()

    first_token = user.auth_token
    first_expiration = user.auth_token_expiration

    assert user.auth_token is not None
    assert user.auth_token_expiration is not None

    user.refresh_auth_token()

    assert user.auth_token is not first_token
    assert user.auth_token_expiration is not first_expiration


def test_generated_token_length():
    """
    Check if the generated token is a
    string of correct length.
    """
    user = User(email="test@mail.com", password="testme")

    user.refresh_auth_token()

    assert len(user.auth_token) == 32


def test_expired_token_returns_no_user(mocker):
    """
    If user's token is expired (date in the past)
    no user should be returned for authentication.
    """
    mocker.patch.object(User, "query", autospec=True)

    user = User(email="test@mail.com", password="testme")
    User.query.filter_by.return_value.first.return_value = user
    now_date = datetime.utcnow()
    past_date = now_date - timedelta(hours=1)
    future_date = now_date + timedelta(hours=1)

    user.auth_token = "token123"
    user.auth_token_expiration = past_date

    looked_up_user = user.get_by_auth_token("token123")

    assert looked_up_user is None

    user.auth_token_expiration = future_date

    looked_up_user = user.get_by_auth_token("token123")

    assert looked_up_user is not None


def test_invalidate_token_removes_token(mocker):
    """
    User's auth token can be invalidated,
    which means it'll be removed from the model.
    """
    user = User(email="test@mail.com", password="testme")

    now_date = datetime.utcnow()
    future_date = now_date + timedelta(hours=1)
    token = "token123"

    user.auth_token = token
    user.auth_token_expiration = future_date

    assert user.auth_token == token
    assert user.auth_token_expiration == future_date

    user.invalidate_auth_token()

    assert user.auth_token is None
    assert user.auth_token_expiration is None
