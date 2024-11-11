import pytest
from app.home.models import Partida
from app.game.carta_figura.models import Carta_Figura

def test_cartas_restantes(test_client, init_db):
    # Crear una partida con 2 jugadores
    partida = Partida(
        nombre="Partida",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Asignar 3 cartas a Jugador1
    cartas = [
        Carta_Figura(id_carta=1, nombre="fig6", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=True),
        Carta_Figura(id_carta=2, nombre="fig5", color="blanca", id_partida=partida.id, id_player="Jugador1", mostrar=False),
        Carta_Figura(id_carta=3, nombre="fig6", color="blanca", id_partida=partida.id, id_player="Jugador2", mostrar=True)
    ]
    db.add_all(cartas)
    db.commit()
    response = test_client.get(f"/game/{partida.id}/carta_figura/cartas_restantes")

    # Verificar que la respuesta sea correcta
    assert response.status_code == 200, f"No se pudo obtener las cartas restantes: {response.text}"
    assert response.json() == [{'cantidad':1 , 'jugador':'Jugador1'},
                                {'cantidad':0 , 'jugador':'Jugador2'}], "El número de cartas restantes es incorrecto"

#no hay cartas asignadas a la partida
def test_cartas_restante_sin_cartas_asignadas(test_client, init_db):
    # Crear una partida con 2 jugadores
    partida = Partida(
        nombre="Partida",
        owner="Jugador1",
        jugador1="Jugador1",
        jugador2="Jugador2",
        max_jugadores=2,
        iniciada=True
    )
    db = init_db
    db.add(partida)
    db.commit()

    # Realizar la petición para obtener las cartas restantes de Jugador1
    response = test_client.get(f"/game/{partida.id}/carta_figura/cartas_restantes")

    # Verificar que la respuesta sea correcta
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay cartas asignadas a la partida"}

#no hay partida
def test_cartas_restante_sin_partida(test_client, init_db):
    # Realizar la petición para obtener las cartas restantes de Jugador1
    response = test_client.get(f"/game/-1/carta_figura/cartas_restantes")

    # Verificar que la respuesta sea correcta
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}