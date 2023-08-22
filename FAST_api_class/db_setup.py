from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URI = 'postgresql://127.0.0.1:5432/employee_db?user=carol&password=1234'
# employee_db vanya db name , user=nameofuser and pw chai afnai pw

engine=create_engine(
    SQL_ALCHEMY_DATABASE_URI, connect_args={},future=True
    
)
SessionLocal=sessionmaker(
    autocommit=False,autoflush=False, bind=engine, future =True
)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()