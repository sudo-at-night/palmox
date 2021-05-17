from models.user import User


def test_login(client, mocker):
    """
    If client provides correct credentials,
    client recieves an authentication token
    in a HTTP-Only cookie.
    """
    mock_user_class = mocker.patch("blueprints.web.blueprint.User")

    user = User(email="test@mail.com", password="testme")
    mock_user_class.query.filter_by.return_value.first.return_value = user

    response = client.post(
        "/login",
        json={
            "email": "test@mail.com",
            "password": "testme",
        },
    )
    cookie_header = response.headers.get("Set-Cookie")

    assert response.status_code == 204
    assert cookie_header is not None
    assert f"FSESSIONID={user.auth_token}; HttpOnly;" in cookie_header


def test_login_failure(client, mocker):
    """
    If client provides incorrect credentials,
    client receives a 401 error response.
    """
    mock_user_class = mocker.patch("blueprints.web.blueprint.User")

    mock_user_class.query.filter_by.return_value.first.return_value = None

    response = client.post(
        "/login",
        json={
            "email": "test@mail.com",
            "password": "testme",
        },
    )

    assert response.status_code == 401
