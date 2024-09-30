// getGameListServices.js: Servicio para obtener la lista de partidas

const API_URL = "https://proyecto-ingenieria-software-i.onrender.com/partida/partidas";

export const getGameListServices = async () => {
  try {
    const response = await fetch(API_URL);

    console.log("Response:", response);
    if (!response.ok) {
      throw new Error("Error al obtener las partidas");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error: con getGameListService", error);
    throw error;
  }
};
