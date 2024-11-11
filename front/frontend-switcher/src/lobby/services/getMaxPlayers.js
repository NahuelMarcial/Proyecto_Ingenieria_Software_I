import URL_API from "../../configs/urlAPI";

const getMaxPlayers = async () => {
  const partida_id = sessionStorage.getItem("partida_id");

  try {
    const response = await fetch(`${URL_API}/home/partida/${partida_id}`);
    if (!response.ok) {
      throw new Error("Error al obtener el número máximo de jugadores");
    }
    const data = await response.json();
    return data.max_jugadores;
  } catch (error) {
    throw new Error("Error: getMaxPlayers");
  }
};

export default getMaxPlayers;
