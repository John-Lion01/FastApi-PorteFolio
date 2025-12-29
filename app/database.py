# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# supabase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# URL pour une base de données SQLite locale
# DATABASE_URL = "sqlite:///./database.db"
DATABASE_URL = os.getenv("SUPABASE_DB_URL")
print("\n \n ***", DATABASE_URL, "\n \n ***")

# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
engine = create_async_engine(
    DATABASE_URL, echo=True
)
print("\n \n ***", engine, "\n \n ***")
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

# Fonction pour obtenir une session de base de données
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

async def get_db():
    async with AsyncSessionLocal() as session :
        yield session