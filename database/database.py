from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SQLite database location
DATABASE_PATH = BASE_DIR / "voice_analyser.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database models
Base = declarative_base()


def init_db():
    """
    Create database tables if they do not already exist.
    """
    from database import models  # Register SQLAlchemy models

    Base.metadata.create_all(bind=engine)