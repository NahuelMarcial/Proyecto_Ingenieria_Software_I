import URL_API from "../../configs/urlAPI";

export const getCurrentTurn = async (partida_id) => {
  try {
    const response = await fetch(URL_API + `/game/${partida_id}/turno_jugador`);
    if (!response.ok) {
      throw new Error("Error al obtener el turno");
    }

    const data = await response.json();
    return data.id_player;
  } catch (error) {
    console.error("Error obteniendo el turno actual:", error);
    return null;
  }
};

export const endTurn = async (partida_id, jugador_id) => {
  try {
    const body = { id_player: jugador_id };
    const response = await fetch(
      URL_API + `/game/${partida_id}/terminar_turno`,
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
      throw new Error("Error al terminar el turno");
    }
    const data = await response.json();
    return data.id_player;
  } catch (error) {
    console.error("Error al terminar el turno:", error);
    throw error;
  }
};

export const getStartTurnTime = async (partida_id) => {
  try {
    const response = await fetch(
      URL_API + `/game/${partida_id}/start_turn_time`,
      {
        method: "GET",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );
    if (!response.ok) {
      throw new Error("Error al obtener el tiempo de inicio del turno");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error: getStartTurnTime", error);
    throw error;
  }
};

export const endTurnTimeOut = async (partida_id) => {
  try {
    const response = await fetch(
      URL_API + `/game/${partida_id}/terminar_turno_timeout`,
      {
        method: "PATCH",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );
    if (!response.ok) {
      throw new Error("Error al terminar el tiempo del turno");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error: endTurnTimeOut", error);
    throw error;
  }
};
