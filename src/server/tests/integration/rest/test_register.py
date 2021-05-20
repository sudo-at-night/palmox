from models.user import User


def test_register(client, mocker, default_credentials):
    """
    If client provides correct credentials
    which have not been used already, and a
    new user can be created client receives
    a 201 error response.
    """
    mock_db_session = mocker.patch("blueprints.web.blueprint.db_session")
    mock_db_session.add.return_value = True
    mock_db_session.commit.return_value = True

    response = client.post(
        "/register",
        json=default_credentials,
    )

    assert response.status_code == 201


def test_register_failure_already_exists(client, mocker, default_credentials):
    """
    If client provides correct credentials
    which have been used already, client
    receives a 409 error response.
    """
    mock_user_class = mocker.patch("blueprints.web.blueprint.User")

    user = User(
        email=default_credentials["email"], password=default_credentials["password"]
    )
    mock_user_class.query.filter_by.return_value.first.return_value = user

    response = client.post(
        "/register",
        json=default_credentials,
    )

    assert response.status_code == 409


def test_register_failure_incorrect_request(client):
    """
    If client provides credentials
    in a wrong form (incorrect request)
    client receives a 400 error response.
    """
    response = client.post(
        "/register",
        json={
            "bad": "request",
            "wrong": "field",
        },
    )

    assert response.status_code == 400


def test_register_failure_incorrect_password_length(client, default_credentials):
    """
    If client provides credentials
    and validation fails (password length)
    client receives a 400 error response.
    """
    credentials = default_credentials
    credentials["password"] = "12"

    response = client.post(
        "/register",
        json=credentials,
    )

    assert response.status_code == 400


def test_register_failure_incorrect_email_format(client, default_credentials):
    """
    If client provides credentials
    and validation fails (email format)
    client receives a 400 error response.
    """
    credentials = default_credentials
    credentials["email"] = "testmewrongemail"

    response = client.post(
        "/register",
        json=credentials,
    )

    assert response.status_code == 400
