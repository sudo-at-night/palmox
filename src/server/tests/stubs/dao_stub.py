class DaoStub:
    """
    A stub for a specific instance of DAO class.
    """

    data_to_return = None

    def __init__(self, data_to_return):
        self.data_to_return = data_to_return

    def get(self, id=""):
        return self.data_to_return

    def get_all(self, id=""):
        return self.data_to_return
