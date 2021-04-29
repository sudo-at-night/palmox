from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.postgres import Base


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    key = Column(String(250), unique=True, index=True, nullable=False)
    name = Column(String(160))
    feature_flags = relationship("FeatureFlag")

    def __init__(self, *, key, name=None, feature_flags=[]):
        self.key = key
        self.name = name
        self.feature_flags = feature_flags

    def __repr__(self):
        return "<Project %r>" % (self.name)
