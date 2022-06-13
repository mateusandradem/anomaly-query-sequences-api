from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from api.config import settings
from api.db.database import Base

test_engine = create_engine(settings.TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autoflush=False, bind=test_engine)


Base.metadata.create_all(bind=test_engine)


def override_get_db():
    connection = test_engine.connect()
    transaction = connection.begin()
    db = Session(bind=connection)
    yield db
    db.rollback()
    connection.close()
