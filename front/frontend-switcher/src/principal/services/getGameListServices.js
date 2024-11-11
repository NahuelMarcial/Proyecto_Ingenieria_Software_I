// getGameListServices.js: Servicio para obtener la lista de partidas
import URL_API from "../../configs/urlAPI";

export const getGameListServices = async (player_id) => {
  try {
    const response = await fetch(URL_API + `/home/partidas/${player_id}`);
    if (!response.ok) {
      throw new Error("Error al obtener las partidas");
    }

    console.log("Partidas actualizadas");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error: con getGameListService", error);
    throw error;
  }
};
