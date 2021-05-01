from unittest.mock import MagicMock
from models.abstract.dao import AbstractExposableDao
from tests.stubs.model_stub import ModelStub


class MockDao(AbstractExposableDao[ModelStub]):
    CACHE_PREFIX = "cache-prefix"

    def _parse_model_to_client_model(self, original_model):
        return {
            "mapped_one": original_model.one,
            "mapped_two": original_model.two,
        }


def test_returns_mapped_client_model(mocker):
    """
    Data is fetched from the database and mapped
    to the client model specified by parse function
    on the concrete class.
    """
    mocker.patch("cache.redis.cache.get", return_value=None)
    mocker.patch("cache.redis.cache.set", return_value=None)

    mock_dao = MockDao()

    returned_data = mock_dao.get("test-1")

    assert returned_data == {
        "mapped_one": 1,
        "mapped_two": 2,
    }


def test_returns_mapped_client_model_from_cache(mocker):
    """
    Fetching of data from the database is skipped
    if cache is hit first.
    """
    mocker.patch(
        "cache.redis.cache.get", return_value={"mapped_one": 15, "mapped_two": 30}
    )

    mock_dao = MockDao()
    mock_dao._parse_model_to_client_model = MagicMock()

    returned_data = mock_dao.get("test-1")

    assert returned_data == {
        "mapped_one": 15,
        "mapped_two": 30,
    }

    mock_dao._parse_model_to_client_model.assert_not_called()


def test_returns_mapped_client_model_all(mocker):
    """
    All data is fetched from the database and mapped
    to the client model specified by parse function
    on the concrete class.
    """
    mocker.patch("cache.redis.cache.get", return_value=None)
    mocker.patch("cache.redis.cache.set", return_value=None)

    mock_dao = MockDao()

    returned_data = mock_dao.get_all()

    assert returned_data == [
        {
            "mapped_one": 1,
            "mapped_two": 2,
        },
        {
            "mapped_one": 1,
            "mapped_two": 2,
        },
    ]


def test_returns_mapped_client_model_from_cache_all(mocker):
    """
    Fetching of data from the database is skipped
    if cache is hit first.
    """
    mocker.patch(
        "cache.redis.cache.get",
        return_value=[
            {"mapped_one": 15, "mapped_two": 30},
            {"mapped_one": 15, "mapped_two": 30},
        ],
    )

    mock_dao = MockDao()
    mock_dao._parse_model_to_client_model = MagicMock()

    returned_data = mock_dao.get("test-1")

    assert returned_data == [
        {
            "mapped_one": 15,
            "mapped_two": 30,
        },
        {
            "mapped_one": 15,
            "mapped_two": 30,
        },
    ]

    mock_dao._parse_model_to_client_model.assert_not_called()


def test_cache_prefix_is_used_query_single(mocker):
    """
    Const variable CACHE_PREFIX is used when resolving cache
    when querying for single result.
    """
    mock_cache_get = mocker.patch("cache.redis.cache.get", return_value=None)
    mock_cache_set = mocker.patch("cache.redis.cache.set", return_value=None)

    mock_dao = MockDao()
    mock_dao.get("test-1")

    mock_cache_get.assert_called_with(f"{MockDao.CACHE_PREFIX}::test-1")
    mock_cache_set.assert_called_with(
        f"{MockDao.CACHE_PREFIX}::test-1", {"mapped_one": 1, "mapped_two": 2}
    )


def test_cache_prefix_is_used_query_all(mocker):
    """
    Const variable CACHE_PREFIX is used when resolving cache
    when querying for all results.
    """
    mock_cache_get = mocker.patch("cache.redis.cache.get", return_value=None)
    mock_cache_set = mocker.patch("cache.redis.cache.set", return_value=None)

    mock_dao = MockDao()
    mock_dao.get_all()

    mock_cache_get.assert_called_with(f"{MockDao.CACHE_PREFIX}::")
    mock_cache_set.assert_called_with(
        f"{MockDao.CACHE_PREFIX}::",
        [{"mapped_one": 1, "mapped_two": 2}, {"mapped_one": 1, "mapped_two": 2}],
    )
