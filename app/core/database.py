# app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# Get URL (fallback to local SQLite for tests/dev)
DATABASE_URL = getattr(settings, "DATABASE_URL", None) or "sqlite:///./test.db"

# SQLite needs this arg when used with FastAPI (threaded)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Engine (fix: pool_recycle spelling)
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args=connect_args,
)

# SQLAlchemy 2.0 declarative base
class Base(DeclarativeBase):
    pass

# Session factory (fix: False is capitalized in Python)
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# FastAPI dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
