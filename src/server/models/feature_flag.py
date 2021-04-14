class FeatureFlag:
    id: str
    name: str
    is_active: bool

    def __init__(self, *, id, name, is_active=False):
        self.id = id
        self.name = name
        self.is_active = is_active
