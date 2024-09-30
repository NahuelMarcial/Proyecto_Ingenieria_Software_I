const API_disconectgamestarted =
  "http://localhost:8000/game/abandonar_partida_ini/";

const Disconectgamestarted = async (game_id, player_id, sid, nav) => {
  try {
    const body = {
      id_player: player_id,
      sid: sid,
    };
    const response = await fetch(API_disconectgamestarted + game_id, {
      method: "PATCH",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      throw new Error("No se pudo abandonar la partida iniciada");
    }
    sessionStorage.removeItem("partida_id");
    sessionStorage.removeItem("players");
    sessionStorage.removeItem("partida_nombre");
    nav("/");
  } catch (e) {
    throw e;
  }
};

export default Disconectgamestarted;
