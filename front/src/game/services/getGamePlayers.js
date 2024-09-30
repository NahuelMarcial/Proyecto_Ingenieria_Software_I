export const getGamePlayers = async (partida_id) => {
  const API_URL = `https://proyecto-ingenieria-software-i.onrender.com/lobby/jugadores/${partida_id}`;
  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error("Error obteniendo la partida");
    }
    const partida = await response.json();

    // Asumimos que la API te devuelve los nombres de los jugadores en jugador1, jugador2, etc.
    const jugadores = [
      partida.jugador1,
      partida.jugador2,
      partida.jugador3,
      partida.jugador4,
    ].filter(Boolean); // Filtramos los jugadores vacíos

    return jugadores; // Devolvemos los jugadores
  } catch (error) {
    console.error("Error fetching partida:", error);
    return [];
  }
};

export default getGamePlayers;
