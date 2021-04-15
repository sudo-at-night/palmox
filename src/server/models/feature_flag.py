from sqlalchemy import Column, Integer, String, Boolean
from db.postgres import Base

class PostgresFeatureFlag(Base):
    __tablename__ = 'feature_flags'
    id = Column(Integer, primary_key=True)
    name = Column(String(160))
    is_active = Column(Boolean)

    def __init__(self, *, name=None, is_active=False):
        self.name = name
        self.is_active = is_active

    def __repr__(self):
        return '<FeatureFlag %r>' % (self.name)

class RedisFeatureFlag:
    id: str
    name: str
    is_active: bool

    def __init__(self, *, id, name, is_active=False):
        self.id = id
        self.name = name
        self.is_active = is_active
