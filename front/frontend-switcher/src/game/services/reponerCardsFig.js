import URL_API from "../../configs/urlAPI";

const reponerCardsFig = async (partida_id, jugador_id) => {
  try {
    const response = await fetch(
      `${URL_API}/game/${partida_id}/carta_figura/reponer_cartas_jugador`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ player_id: jugador_id }),
      }
    );
  } catch (error) {
    console.error("Error al reponer cartas figura", error);
    throw error;
  }
};

export default reponerCardsFig;
