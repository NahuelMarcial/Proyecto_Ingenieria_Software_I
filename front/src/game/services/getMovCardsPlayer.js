export const getMovCardsPlayer = async (partida_id, jugador_id) => {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/carta_movimiento/get_cartas_jugador/` +
        partida_id +
        "/" +
        jugador_id,
      {
        method: "GET",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );
    if (response.ok !== true) {
      throw new Error(
        "No se pudo obtener las cartas movimiento del jugador " + jugador_id
      );
    }

    let movCards = await response.json();
    return movCards;
  } catch {
    console.error("Error: getMovCardsPlayer.");
    throw error;
  }
};

export default getMovCardsPlayer;
