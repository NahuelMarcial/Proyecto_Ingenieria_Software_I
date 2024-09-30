import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.partida.models import Partida
from app.main import app
from app.database.database import Base, get_db
from app.carta_figura.models import Carta_Figura
import json

# Configuración para la base de datos de prueba
TEST_DB_NAME = "test.db"
TEST_DB_DIRECTORY = "data_bases"
TEST_DB_URL = f"sqlite:///{TEST_DB_DIRECTORY}/{TEST_DB_NAME}"

# Crear el directorio si no existe
if not os.path.exists(TEST_DB_DIRECTORY):
    os.makedirs(TEST_DB_DIRECTORY)

# Crear el motor y la sesión para la base de datos de prueba
test_engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Crear todas las tablas en la base de datos de prueba
Base.metadata.create_all(bind=test_engine)

# Sobrescribir la dependencia de la base de datos para que use la base de datos de test
def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def test_client():
    yield TestClient(app)

@pytest.fixture(scope="module")
def init_db():
    db = TestSessionLocal()
    
    db.commit()
    
    yield db
    db.close()
