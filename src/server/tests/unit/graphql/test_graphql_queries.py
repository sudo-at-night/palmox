from graphene.test import Client
from blueprints.exposable.gql import schema
from tests.stubs.dao_stub import DaoStub


def test_feature_flag(mocker):
    """
    Feature flags are queried and returned correctly.
    """
    DaoMock = DaoStub({"key": "test-flag", "name": "Test Flag", "is_active": True})
    mocker.patch("blueprints.exposable.gql.FeatureFlagDao", return_value=DaoMock)
    client = Client(schema)

    query = client.execute(
        """
        {
            featureFlag(key: "test-flag") {
                key
                name
                isActive
            }
        }
        """
    )

    assert query == {
        "data": {
            "featureFlag": {"key": "test-flag", "name": "Test Flag", "isActive": True}
        }
    }

    DaoMock = DaoStub([{"key": "test-flag", "name": "Test Flag", "is_active": True}])
    mocker.patch("blueprints.exposable.gql.FeatureFlagDao", return_value=DaoMock)

    query = client.execute(
        """
        {
            featureFlags {
                key
                name
                isActive
            }
        }
        """
    )

    assert query == {
        "data": {
            "featureFlags": [
                {"key": "test-flag", "name": "Test Flag", "isActive": True}
            ]
        }
    }


def test_project(mocker):
    """
    Projects are queried and returned correctly.
    """
    DaoMock = DaoStub(
        {"key": "test-project", "name": "Test Project", "feature_flags": []}
    )
    mocker.patch("blueprints.exposable.gql.ProjectDao", return_value=DaoMock)
    client = Client(schema)

    query = client.execute(
        """
        {
            project(key: "test-project") {
                key
                name
                featureFlags {
                    name
                }
            }
        }
        """
    )

    assert query == {
        "data": {
            "project": {
                "key": "test-project",
                "name": "Test Project",
                "featureFlags": [],
            }
        }
    }

    DaoMock = DaoStub(
        [{"key": "test-project", "name": "Test Project", "feature_flags": []}]
    )
    mocker.patch("blueprints.exposable.gql.ProjectDao", return_value=DaoMock)

    query = client.execute(
        """
        {
            projects {
                key
                name
                featureFlags {
                    name
                }
            }
        }
        """
    )

    assert query == {
        "data": {
            "projects": [
                {"key": "test-project", "name": "Test Project", "featureFlags": []}
            ]
        }
    }
