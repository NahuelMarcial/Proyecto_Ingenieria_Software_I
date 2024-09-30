// src/services/gameService.js

const API_abandonar_partida = "http://localhost:8000/lobby/abandonar/";

export const abandonarPartida = async (gameid, playerid, sid, nav) => {
  try {
    const bodyinfo = {
      jugador: playerid,
      sid: sid,
    };
    const response1 = await fetch(API_abandonar_partida + gameid, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(bodyinfo),
    });
    if (!response1.ok) {
      throw new Error("Error al abandonar la partida");
    }
    nav("/");

    const respuesta = await response1.json();
    return respuesta;
  } catch (error) {
    console.error("ERROR:", error);
    throw error;
  }
};

export default abandonarPartida;
