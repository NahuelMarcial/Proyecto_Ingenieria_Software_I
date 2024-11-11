import URL_API from "../../configs/urlAPI";

export const getPlayerListService = async (partida_id) => {
  try {
    // Realizamos el fetch a la URL con el id de la partida
    const response = await fetch(URL_API + `/lobby/${partida_id}/jugadores`, {
      method: "GET", // Solicitud GET para obtener la lista
      headers: {
        "Content-Type": "application/json", // Aseguramos que enviamos y recibimos JSON
      },
    });
    // Verificamos si la respuesta fue exitosa
    if (!response.ok) {
      throw new Error(`Error al obtener los jugadores: ${response.statusText}`);
    }
    // Parseamos la respuesta a JSON
    const data = await response.json();

    return data; // Devolvemos la lista de jugadores
  } catch (error) {
    console.error("Error en fetchJugadores:", error);
  }
};

export default getPlayerListService;
