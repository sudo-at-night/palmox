def test_logout(client):
    """
    Removes the HTTP-Only cookie with
    authentication token.
    """
    response = client.get(
        "/logout",
    )
    cookie_header = response.headers.get("Set-Cookie")

    assert response.status_code == 204
    assert cookie_header is not None
    assert "HttpOnly;" in cookie_header
    assert "FSESSIONID=; Expires=Thu, 01 Jan 1970 00:00:00 GMT;" in cookie_header
