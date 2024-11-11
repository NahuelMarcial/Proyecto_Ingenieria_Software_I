import pytest
from app.home.models import Partida

#Test para verificar que el color prohido sea correcto

#caso exitoso 
def test_color_prohibido_azul(test_client,init_db): 
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True,
        cantidad_jugadores=2,
        turno=2,
        color_bloqueado="azul"
    )

    db = init_db
    db.add(partida)
    db.commit()
    
    response = test_client.get(f"/game/{partida.id}/color_prohido")
    color_prohibido = response.json()
    assert response.status_code == 200,"Error al obtener el color prohibido azul"
    assert color_prohibido == {"color": "azul"} , "Se esperaba color azul pero se obtuvo otro color"

def test_color_prohibido_rojo(test_client,init_db):
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True,
        cantidad_jugadores=2,
        turno=2,
        color_bloqueado="rojo"
    )

    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/color_prohido")
    color_prohibido = response.json()
    assert response.status_code == 200,"Error al obtener el color prohibido rojo"
    assert color_prohibido == {"color": "rojo"}, "Se esperaba color rojo pero se obtuvo otro color"

def test_color_prohibido_verde(test_client,init_db):
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True,
        cantidad_jugadores=2,
        turno=2,
        color_bloqueado="verde"
    )

    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/color_prohido")
    color_prohibido = response.json()
    assert response.status_code == 200,"Error al obtener el color prohibido verde"
    assert color_prohibido == {"color": "verde"},"Se esperaba color verde pero se obtuvo otro color"

def test_color_prohibido_amarillo(test_client,init_db):
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True,
        cantidad_jugadores=2,
        turno=2,
        color_bloqueado="amarillo"
    )

    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/color_prohido")
    color_prohibido = response.json()
    assert response.status_code == 200,"Error al obtener el color prohibido amarillo"
    assert color_prohibido == {"color": "amarillo"},"Se esperaba color amarillo pero se obtuvo otro color"

def test_color_prohibido_no_color(test_client,init_db):
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True,
        cantidad_jugadores=2,
        turno=2,
        color_bloqueado=""
    )

    db = init_db
    db.add(partida)
    db.commit()

    
    response = test_client.get(f"/game/{partida.id}/color_prohido")
    color_prohibido = response.json()
    assert response.status_code == 200,"Error al obtener el color prohibido"
    assert color_prohibido == {"color": ""},"Se esperaba color \"\" pero se obtuvo otro color"

#casos fallidos 
def test_color_prohibido_partida_no_existe(test_client, init_db):
    response = test_client.get(f"/game/999999999999999/color_prohido")
    assert response.status_code == 404,"Se esperaba error 404 ya que la partida no existe"
    assert response.json() == {"detail": "Partida no encontrada"}


def test_color_prohibido_partida_no_iniciada(test_client,init_db):
    partida = Partida(
        nombre="Partida Test",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=False,
        cantidad_jugadores=2,
        turno=2,
        color_bloqueado="azul"
    )

    db = init_db
    db.add(partida)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/color_prohido")
    assert response.status_code == 400,"Se esperaba error 400 ya que la partida no esta inicida"
    assert response.json() == {"detail": "La partida no ha iniciado"}


