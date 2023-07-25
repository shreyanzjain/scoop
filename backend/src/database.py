from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# CREATE YOUR 'env.py' FILE IN 'backend' AND DEFINE THESE VARIABLES AS PER YOUR POSTGRES CONFIG
# PGUSR = Postgres user to log in
# PGPASSWD = Postgres password for the aforesaid user
# DBNAME =  Name of the db you want to access

from env import PGUSR, PGPASSWD, DBNAME

SQL_DATABASE_URL = f"postgresql://{PGUSR}:{PGPASSWD}@localhost/{DBNAME}"

engine = create_engine(SQL_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()