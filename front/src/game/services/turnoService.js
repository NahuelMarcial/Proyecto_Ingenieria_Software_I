export const getCurrentTurn = async (partida_id) => {
  try {
    const response = await fetch(
      `http://localhost:8000/game/turno_jugador/` + partida_id
    );
    if (!response.ok) {
      throw new Error("Error al obtener el turno");
    }

    const data = await response.json();
    console.log("Turno actual:", data);

    return data.id_player;
  } catch (error) {
    console.error("Error obteniendo el turno actual:", error);
    return null;
  }
};

export const endTurn = async (partida_id, jugador_id) => {
  try {
    const body = { id_player: jugador_id };
    console.log("Body enviado:", body);
    const response = await fetch(
      `http://localhost:8000/game/terminar_turno/` + partida_id,
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
    return null;
  }
};
