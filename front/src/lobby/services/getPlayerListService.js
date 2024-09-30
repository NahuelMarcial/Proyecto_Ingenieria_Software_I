export const getPlayerListService = async (partida_id) => {
  try {
    // Realizamos el fetch a la URL con el id de la partida
    const response = await fetch(
      `https://proyecto-ingenieria-software-i.onrender.com/lobby/jugadores/${partida_id}`,
      {
        method: "GET", // Solicitud GET para obtener la lista
        headers: {
          "Content-Type": "application/json", // Aseguramos que enviamos y recibimos JSON
        },
      }
    );
    console.log("Respuesta de fetchJugadores:", response.body);
    // Verificamos si la respuesta fue exitosa
    if (!response.ok) {
      throw new Error(`Error al obtener los jugadores: ${response.statusText}`);
    }

    // Parseamos la respuesta a JSON
    const data = await response.json();
    console.log("Lista de jugadores:", data);

    return data; // Devolvemos la lista de jugadores
  } catch (error) {
    console.error("Error en fetchJugadores:", error);
  }
};

export default getPlayerListService;
