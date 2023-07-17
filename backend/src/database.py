from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# From env.py 
from env import PGUSR, PGPASSWD, DBNAME

SQL_DATABASE_URL = f"postgresql://{PGUSR}:{PGPASSWD}@localhost/{DBNAME}"

engine = create_engine(SQL_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()