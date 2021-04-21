from sqlalchemy import Column, Integer, String, Boolean
from db.postgres import Base

class PostgresFeatureFlag(Base):
    __tablename__ = 'feature_flags'
    id = Column(Integer, primary_key=True)
    key = Column(String(250), unique=True, index=True, nullable=False)
    name = Column(String(160))
    is_active = Column(Boolean)

    def __init__(self, *, key, name=None, is_active=False):
        self.key = key
        self.name = name
        self.is_active = is_active

    def __repr__(self):
        return '<FeatureFlag %r>' % (self.name)

class RedisFeatureFlag:
    key: str
    name: str
    is_active: bool

    def __init__(self, *, key, name, is_active=False):
        self.key = key
        self.name = name
        self.is_active = is_active
