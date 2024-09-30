import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# Configuración para SQLite
DB_NAME = os.getenv("DB_NAME")
db_directory = "data_bases"

# Crear el directorio si no existe
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Crear la URL completa con la ruta del archivo
URL = "sqlite:///{}/{}".format(db_directory, DB_NAME)

engine = create_engine(URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_all():
    Base.metadata.create_all(bind=engine)

def drop_all():
    Base.metadata.drop_all(bind=engine)
