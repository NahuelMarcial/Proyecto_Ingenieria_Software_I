export const getFigCardsPlayer = async (partida_id, jugador_id) => {
  try {
    const response = await fetch(
      `https://proyecto-ingenieria-software-i.onrender.com/carta_figura/mano_jugador/` +
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
        "No se pudo obtener las cartas figura del jugador " + jugador_id
      );
    }
    let figCards = await response.json();
    return figCards;
  } catch (error) {
    console.error("Error: getFigCardsPlayer.", error);
    throw error;
  }
};

export default getFigCardsPlayer;
