from datetime import datetime, timedelta
from models.user import User


def test_logout_remove_cookie(client):
    """
    Removes the HTTP-Only cookie with
    authentication token.
    """
    client.set_cookie("", "FSESSIONID", "abc123")
    response = client.get(
        "/logout",
    )
    cookie_header = response.headers.get("Set-Cookie")

    assert response.status_code == 204
    assert cookie_header is not None
    assert "HttpOnly;" in cookie_header
    assert "FSESSIONID=; Expires=Thu, 01 Jan 1970 00:00:00 GMT;" in cookie_header


def test_logout_user_query(client, mocker):
    """
    Session ID is looked up to invalidate
    it in the database.
    """
    mock_user_class = mocker.patch("blueprints.web.blueprint.User")
    request_auth_token = "abc123"

    now_date = datetime.utcnow()
    future_date = now_date + timedelta(hours=1)

    user = User(email="test@mail.com", password="testme")
    user.auth_token = request_auth_token
    user.auth_token_expiration = future_date
    user.invalidate_auth_token = mocker.MagicMock()

    mock_user_class.get_by_auth_token.return_value = user

    client.set_cookie("", "FSESSIONID", request_auth_token)
    client.get(
        "/logout",
    )

    mock_user_class.get_by_auth_token.assert_called_with(request_auth_token)
    user.invalidate_auth_token.assert_called()
