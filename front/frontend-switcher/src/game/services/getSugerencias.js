import URL_API from "../../configs/urlAPI";

const getSugerencias = async () => {
  try {
    const partida_id = sessionStorage.getItem("partida_id");
    const player_id = sessionStorage.getItem("jugador_id");

    const response = await fetch(
      `${URL_API}/game/${partida_id}/fichas/get_sugerencias/${player_id}`
    );
    const data = await response.json();
    console.log("Sugerencias obtenidas:", data);
    return data;
  } catch (error) {
    console.error("Error al obtener las sugerencias:", error);
    return;
  }
};

export default getSugerencias;
