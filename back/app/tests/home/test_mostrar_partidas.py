from app.home.schemas import PartidaData, PartidaGet

def test_mostar_partidas(test_client):

    response = test_client.get("/home/partidas/test_player")
    assert response.status_code == 200 ,"Error al obtener las partidas"

    # Verificar que el JSON de la respuesta sea una lista de PartidaData
    partidas = response.json()
    assert isinstance(partidas, list) ,"La partida no es una lista"
    for partida in partidas:
        assert PartidaGet(**partida),"La partida no es de tipo PartidaGet"


def test_partidas_iniciadas(test_client):

    response = test_client.get("/home/partidas/test_player")
    assert response.status_code == 200,"Error al obtener las partidas"

    # Verificar que solo se devuelvan partidas no iniciadas
    partidas = response.json()
    assert isinstance(partidas, list) ,"La partida no es una lista"
    for partida in partidas:
        assert not partida['iniciada'] ,"Hay una partida iniciada"


def test_partidas_llenas(test_client):

    response = test_client.get("/home/partidas/test_player")
    assert response.status_code == 200 ,"Error al obtener las partidas"

    # Verificar que solo se devuelvan partidas no llenas
    partidas = response.json()
    assert isinstance(partidas, list)
    for partida in partidas:
        assert partida["cantidad_jugadores"] < partida["max_jugadores"] ,"Hay una partida llena"
    