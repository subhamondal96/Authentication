from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
# Replace with your actual MySQL credentials
DATABASE_URL = "mysql+pymysql://root:Pranab123%40@localhost/transglobal"
=======

DATABASE_URL = "mysql+pymysql://root:Subha1234@localhost/transglobal"
>>>>>>> b61b1ae3f8165226c065889187c3f7a281172bfe

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
