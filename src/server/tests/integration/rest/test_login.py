from models.user import User


def test_login(client, mocker, default_credentials):
    """
    If client provides correct credentials,
    client receives an authentication token
    in a HTTP-Only cookie.
    """
    mock_user_class = mocker.patch("blueprints.web.blueprint.User")

    user = User(
        email=default_credentials["email"], password=default_credentials["password"]
    )
    mock_user_class.query.filter_by.return_value.first.return_value = user

    response = client.post(
        "/login",
        json=default_credentials,
    )
    cookie_header = response.headers.get("Set-Cookie")

    assert response.status_code == 204
    assert cookie_header is not None
    assert f"FSESSIONID={user.auth_token}; HttpOnly;" in cookie_header


def test_login_failure_incorrect_credentials(client, mocker, default_credentials):
    """
    If client provides incorrect credentials,
    client receives a 401 error response.
    """
    mock_user_class = mocker.patch("blueprints.web.blueprint.User")

    mock_user_class.query.filter_by.return_value.first.return_value = None

    response = client.post(
        "/login",
        json=default_credentials,
    )

    assert response.status_code == 401


def test_login_failure_bad_request(client, default_credentials):
    """
    If client provides credentials
    in a wrong form (incorrect request)
    client receives a 400 error response.
    """
    credentials = default_credentials
    credentials["password"] = "12"

    response = client.post(
        "/login",
        json=credentials,
    )

    assert response.status_code == 400


def test_login_failure_incorrect_password_length(client, default_credentials):
    """
    If client provides credentials
    and validation fails (password length)
    client receives a 400 error response.
    """
    credentials = default_credentials
    credentials["password"] = "12"

    response = client.post(
        "/login",
        json=credentials,
    )

    assert response.status_code == 400


def test_login_failure_incorrect_email_format(client, default_credentials):
    """
    If client provides credentials
    and validation fails (email format)
    client receives a 400 error response.
    """
    credentials = default_credentials
    credentials["email"] = "testmewrongemail"

    response = client.post(
        "/login",
        json=credentials,
    )

    assert response.status_code == 400
