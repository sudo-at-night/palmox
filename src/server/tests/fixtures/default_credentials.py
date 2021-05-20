import pytest
from typing import Dict


@pytest.fixture
def default_credentials() -> Dict[str, str]:
    """
    Returns default credentials
    used for easier reuse across
    tests in the project.
    """
    return {
        "email": "test@mail.com",
        "password": "testme",
    }
