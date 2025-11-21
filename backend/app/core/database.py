from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv, find_dotenv
import os

# Load .env
load_dotenv(find_dotenv())

# Get DB URL
DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL =", DATABASE_URL)

# Create engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Base (IMPORTANT!)
Base = declarative_base()

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
