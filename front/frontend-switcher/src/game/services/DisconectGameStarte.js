import URL_API from "../../configs/urlAPI";

const Disconectgamestarted = async (partida_id, player_id, sid, nav) => {
  try {
    const body = {
      id_player: player_id,
      sid: sid,
    };
    const response = await fetch(
      URL_API + `/game/${partida_id}/abandonar_partida_ini`,
      {
        method: "PATCH",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      }
    );
    if (!response.ok) {
      throw new Error("No se pudo abandonar la partida iniciada");
    }
    sessionStorage.removeItem("partida_id");
    sessionStorage.removeItem("partida_nombre");
    sessionStorage.removeItem("turnStartTime");
    nav("/");
  } catch (e) {
    throw e;
  }
};

export default Disconectgamestarted;
