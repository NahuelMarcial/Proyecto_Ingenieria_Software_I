import URL_API from "../../configs/urlAPI";

export const getMovCardsPlayer = async (partida_id, player_id) => {
  try {
    const response = await fetch(
      URL_API +
        `/game/${partida_id}/carta_movimiento/get_cartas_jugador/${player_id}`,
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
        "No se pudo obtener las cartas movimiento del jugador " + player_id
      );
    }

    let movCards = await response.json();
    return movCards;
  } catch (error) {
    console.error("Error: getMovCardsPlayer.");
    throw error;
  }
};

export default getMovCardsPlayer;
