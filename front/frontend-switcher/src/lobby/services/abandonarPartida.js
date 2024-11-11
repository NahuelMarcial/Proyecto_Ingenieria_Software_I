// src/services/gameService.js
import URL_API from "../../configs/urlAPI";

export const abandonarPartida = async (gameid, playerid, sid) => {
  try {
    const bodyinfo = {
      jugador: playerid,
      sid: sid,
    };
    const response1 = await fetch(URL_API + "/lobby/" + gameid + "/abandonar", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(bodyinfo),
    });
    if (!response1.ok) {
      throw new Error("Error al abandonar la partida");
    }
    const respuesta = await response1.json();
    return respuesta;
  } catch (error) {
    console.error("ERROR:", error);
    throw error;
  }
};

export default abandonarPartida;
