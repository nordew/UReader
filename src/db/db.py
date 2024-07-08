import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = Config()

logger.info("init db with URL: %s", config.DATABASE_URL)
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    logger.info("Creating new database session")
    db = SessionLocal()
    try:
        yield db
    finally:
        logger.info("Closing database session")
        db.close()
