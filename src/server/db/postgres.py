from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

config = dotenv_values(".env")
db_user = config["POSTGRES_USER"]
db_password = config["POSTGRES_PASSWORD"]
db_name = config["POSTGRES_DB_NAME"]

engine = create_engine(f"postgresql://{db_user}:{db_password}@db/{db_name}")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models.user import User
    from models.feature_flag import FeatureFlag
    from models.project import Project

    Base.metadata.create_all(bind=engine)
