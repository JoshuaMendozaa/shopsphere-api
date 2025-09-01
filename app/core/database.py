from sqlalchemy import create_engine
from sqlaclemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

#Create the SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recyle=3600,  # Recycle connections every hour
)

#Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=false, bind=engine)

#Create Base class for models
Base = declarative_base()

#Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()