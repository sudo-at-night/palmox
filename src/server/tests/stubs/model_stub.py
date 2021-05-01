class ModelFilterResultDataStub:
    key = "test-1"
    one = 1
    two = 2
    three = 3


class ModelFilterResultStub:
    def first(self):
        return ModelFilterResultDataStub()


class ModelStub:
    """
    A stub for an SQLAlchemy model.
    """

    class query:
        def filter_by(key):
            return ModelFilterResultStub()

        def all():
            return [ModelFilterResultDataStub(), ModelFilterResultDataStub()]
