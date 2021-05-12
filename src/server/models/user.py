import os
import base64
from datetime import datetime, timedelta
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from auth.argon import hasher
from sqlalchemy import Column, String, DateTime
from db.postgres import Base


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(101), nullable=False)
    auth_token = Column(String(32), unique=True, index=True)
    auth_token_expiration = Column(DateTime())

    def __init__(self, *, email: str, password: str):
        self.email = email
        self.password = hasher.hash(password)

    def __repr__(self):
        return "<User %r>" % (self.email)

    def refresh_auth_token(self):
        now = datetime.utcnow()
        self.auth_token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.auth_token_expiration = now + timedelta(hours=24)

    def check_password(self, password):
        return hasher.verify(self.password, password)

    @staticmethod
    def get_by_auth_token(token: str):
        user = User.query.filter_by(auth_token=token).first()
        if user is None or user.auth_token_expiration < datetime.utcnow():
            return None
        return user
