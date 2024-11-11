from app.home.models import Partida
from app.game.fichas.models import Ficha

def test_recon_fige1_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Norte
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige1", "La figura formada no es fige1"


def test_recon_fige1_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Este
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige1", "La figura formada no es fige1"



def test_recon_fige2(test_client, init_db):
    partida = Partida(nombre="Partida Valida",iniciada=True, owner="Jugador1",jugador1="Jugador1", jugador2= 'Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=1, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige2", "La figura formada no es fige2"

def test_recon_fige3_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige3", "La figura formada no es fige3"


def test_recon_fige3_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=6, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=7, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=8, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige3", "La figura formada no es fige3"


def test_recon_fige4_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige4", "La figura formada no es fige4"


def test_recon_fige4_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige4", "La figura formada no es fige4"


def test_recon_fige4_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige4", "La figura formada no es fige4"


def test_recon_fige4_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige4", "La figura formada no es fige4"


def test_recon_fige5_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=0, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige5", "La figura formada no es fige5"


def test_recon_fige5_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige5", "La figura formada no es fige5"


def test_recon_fige5_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige5", "La figura formada no es fige5"


def test_recon_fige5_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige5", "La figura formada no es fige5"


def test_recon_fige6_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=5, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige6", "La figura formada no es fige6"


def test_recon_fige6_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige6", "La figura formada no es fige6"


def test_recon_fige7_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige7", "La figura formada no es fige7"


def test_recon_fige7_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige7", "La figura formada no es fige7"


def test_recon_fige7_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige7", "La figura formada no es fige7"


def test_recon_fige7_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fige7", "La figura formada no es fige7"

def test_recon_fig1_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Definir las fichas en la posición que forman la figura fig1_n
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()
    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig1", "La figura formada no es fig1"

def test_recon_fig1_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Definir las fichas en la posición que forman la figura fig1_s
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=0, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()
    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig1", "La figura formada no es fig1"

def test_recon_fig1_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Definir las fichas en la posición que forman la figura fig1_e
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()
    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig1", "La figura formada no es fig1"

def test_recon_fig1_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # Definir las fichas en la posición que forman la figura fig1_o
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()
    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig1", "La figura formada no es fig1"

def test_recon_fig2_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig2", "La figura formada no es fig2"

def test_recon_fig2_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=0, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig2", "La figura formada no es fig2"

def test_recon_fig2_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig2", "La figura formada no es fig2"

def test_recon_fig2_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig2", "La figura formada no es fig2"

def test_recon_fig3_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig3", "La figura formada no es fig3"

def test_recon_fig3_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig3", "La figura formada no es fig3"

def test_recon_fig3_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig3", "La figura formada no es fig3"

def test_recon_fig3_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig3", "La figura formada no es fig3"

def test_recon_fig4_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig4", "La figura formada no es fig4"

def test_recon_fig4_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=0, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig4", "La figura formada no es fig4"

def test_recon_fig4_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig4", "La figura formada no es fig4"

def test_recon_fig4_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig4", "La figura formada no es fig4"

def test_recon_fig5_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=5, pos_y=2, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=6, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig5", "La figura formada no es fig5"
    

def test_recon_fig5_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=6, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig5", "La figura formada no es fig5"

def test_recon_fig6_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig6", "La figura formada no es fig6"


def test_recon_fig6_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=0, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig6", "La figura formada no es fig6"


def test_recon_fig6_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig6", "La figura formada no es fig6"


def test_recon_fig6_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig6", "La figura formada no es fig6"

def test_recon_fig7_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=5, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig7", "La figura formada no es fig7"


def test_recon_fig7_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=5, pos_y=2, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig7", "La figura formada no es fig7"


def test_recon_fig7_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig7", "La figura formada no es fig7"


def test_recon_fig7_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig7", "La figura formada no es fig7"

def test_recon_fig8_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=5, pos_y=2, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig8", "La figura formada no es fig8"


def test_recon_fig8_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig8", "La figura formada no es fig8"


def test_recon_fig8_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig8", "La figura formada no es fig8"


def test_recon_fig8_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig8", "La figura formada no es fig8"

def test_recon_fig9_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig9", "La figura formada no es fig9"


def test_recon_fig9_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig9", "La figura formada no es fig9"


def test_recon_fig9_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig9", "La figura formada no es fig9"


def test_recon_fig9_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig9", "La figura formada no es fig9"

def test_recon_fig10_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig10", "La figura formada no es fig10"


def test_recon_fig10_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig10", "La figura formada no es fig10"

def test_recon_fig11_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig11", "La figura formada no es fig11"


def test_recon_fig11_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig11", "La figura formada no es fig11"


def test_recon_fig11_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig11", "La figura formada no es fig11"


def test_recon_fig11_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig11", "La figura formada no es fig11"

def test_recon_fig12_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=1, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig12", "La figura formada no es fig12"


def test_recon_fig12_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=5, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig12", "La figura formada no es fig12"

def test_recon_fig13_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig13", "La figura formada no es fig13"


def test_recon_fig13_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=5, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=6, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig13", "La figura formada no es fig13"


def test_recon_fig13_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=6, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig13", "La figura formada no es fig13"


def test_recon_fig13_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=5, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=5, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=6, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig13", "La figura formada no es fig13"

def test_recon_fig14_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=5, pos_y=2, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig14", "La figura formada no es fig14"

def test_recon_fig14_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig14", "La figura formada no es fig14"

def test_recon_fig14_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig14", "La figura formada no es fig14"

def test_recon_fig14_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=5, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig14", "La figura formada no es fig14"

def test_recon_fig15_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig15", "La figura formada no es fig15"

def test_recon_fig15_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig15", "La figura formada no es fig15"

def test_recon_fig15_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig15", "La figura formada no es fig15"

def test_recon_fig15_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=1, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig15", "La figura formada no es fig15"

def test_recon_fig16_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig16", "La figura formada no es fig16"

def test_recon_fig16_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=4, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig16", "La figura formada no es fig16"

def test_recon_fig16_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig16", "La figura formada no es fig16"

def test_recon_fig16_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig16", "La figura formada no es fig16"

def test_recon_fig17(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig17", "La figura formada no es fig17"

def test_recon_fig18_n(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=1, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig18", "La figura formada no es fig18"

def test_recon_fig18_s(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=4, pos_y=2, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig18", "La figura formada no es fig18"

def test_recon_fig18_e(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=3, pos_y=2, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig18", "La figura formada no es fig18"

def test_recon_fig18_o(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 1, "Se esperaba una figura formada"
    assert response_json[0]["figura"] == "fig18", "La figura formada no es fig18"

def test_recon_no_fig(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=1, pos_y=1, color="rojo")

    db.add(ficha1)
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 0, "No se esperaba ninguna figura formada"
    assert response_json == [], "No se esperaba ninguna figura formada"

def test_fig_color_bloqueado(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4, color_bloqueado="rojo")
    db = init_db
    db.add(partida)
    db.commit()

    # fig18 de color bloqueado
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 0, "No se esperaba ninguna figura formada"
    assert response_json == [], "No se esperaba ninguna figura formada"

def test_recon_varias_figuras(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()

    # fig18
    ficha1 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=2, pos_y=2, color="rojo")
    ficha2 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=2, pos_y=3, color="rojo")
    ficha3 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=3, pos_y=3, color="rojo")
    ficha4 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=2, pos_y=4, color="rojo")
    ficha5 = Ficha(id_ficha=5, id_partida=partida.id, pos_x=3, pos_y=4, color="rojo")

    # fige4
    ficha6 = Ficha(id_ficha=1, id_partida=partida.id, pos_x=5, pos_y=5, color="azul")
    ficha7 = Ficha(id_ficha=2, id_partida=partida.id, pos_x=6, pos_y=6, color="azul")
    ficha8 = Ficha(id_ficha=3, id_partida=partida.id, pos_x=5, pos_y=6, color="azul")
    ficha9 = Ficha(id_ficha=4, id_partida=partida.id, pos_x=4, pos_y=6, color="azul")

    db.add_all([ficha1, ficha2, ficha3, ficha4, ficha5, ficha6, ficha7, ficha8, ficha9])
    db.commit()

    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 200, "Error al reconocer figuras"

    response_json = response.json()

    assert len(response_json) == 2, "Se esperaban dos figuras formadas"
    assert response_json[0]["figura"] == "fig18", "La figura formada no es fig18"
    assert response_json[1]["figura"] == "fige4", "La figura formada no es fige4"


def test_recon_figuras_no_iniciada(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=False, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 400
    assert response.json() == {"detail": "La partida no ha iniciado"}

def test_recon_figuras_no_existe_partida(test_client, init_db):
    response = test_client.get(f"/game/999999999/fichas/buscar_figuras_formadas")
    assert response.status_code == 404
    assert response.json() == {"detail": "Partida no encontrada"}

def test_recon_figuras_no_fichas(test_client, init_db):
    partida = Partida(nombre="Partida Valida", iniciada=True, owner="Jugador1", jugador1="Jugador1", jugador2='Jugador2', max_jugadores=4)
    db = init_db
    db.add(partida)
    db.commit()
    response = test_client.get(f"/game/{partida.id}/fichas/buscar_figuras_formadas")
    assert response.status_code == 400
    assert response.json() == {"detail": "No hay fichas asignadas a esta partida"}