import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import socketio

from app.main import app
from app.partida.schemas import PartidaData
from app.database.database import Base, get_db
from app.partida.models import Partida


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
    with patch("app.database.database.get_db", return_value=TestSessionLocal()):
        # Crear una sesión y añadir partidas de prueba
        db = TestSessionLocal()
        partida1 = Partida(nombre="Partida Valida", owner="Jugador1", iniciada=False, cantidad_jugadores=1, max_jugadores=4)
        partida2 = Partida(nombre="Partida Iniciada", owner="Jugador2", iniciada=True, cantidad_jugadores=4, max_jugadores=4)
        db.add(partida1)
        db.add(partida2)
        db.commit()
        yield TestClient(app)
        db.close()

@pytest.fixture(scope="module")
def sio_client():
    sio = socketio.Client()
    sio.connect('http://localhost:8000', socketio_path='/sockets/socket_connection')
    yield sio
    sio.disconnect()

@pytest.fixture
def mock_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


#TODO : no mostrar partidas llenas ni ni iniciadas 
def test_mostar_partidas(test_client):

    response = test_client.get("/partida/partidas/")
    assert response.status_code == 200

    # Verificar que el JSON de la respuesta sea una lista de PartidaData
    partidas = response.json()
    assert isinstance(partidas, list)
    for partida in partidas:
        assert PartidaData(**partida)


def test_partidas_iniciadas(test_client):

    response = test_client.get("/partida/partidas/")
    assert response.status_code == 200

    # Verificar que solo se devuelvan partidas no iniciadas
    partidas = response.json()
    assert isinstance(partidas, list)
    for partida in partidas:
        assert not partida['iniciada']


def test_partidas_llenas(test_client):

    response = test_client.get("/partida/partidas/")
    assert response.status_code == 200

    # Verificar que solo se devuelvan partidas no llenas
    partidas = response.json()
    assert isinstance(partidas, list)
    for partida in partidas:
        assert partida["cantidad_jugadores"] < partida["max_jugadores"]