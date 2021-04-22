from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db.postgres import Base


class PostgresFeatureFlag(Base):
    __tablename__ = "feature_flag"
    id = Column(Integer, primary_key=True)
    key = Column(String(250), unique=True, index=True, nullable=False)
    name = Column(String(160))
    is_active = Column(Boolean)
    project = Column(Integer, ForeignKey("project.id"))

    def __init__(self, *, key, name=None, is_active=False, project):
        self.key = key
        self.name = name
        self.is_active = is_active
        self.project = project

    def __repr__(self):
        return "<FeatureFlag %r>" % (self.name)


class RedisFeatureFlag:
    key: str
    name: str
    is_active: bool

    def __init__(self, *, key, name, is_active):
        self.key = key
        self.name = name
        self.is_active = is_active
