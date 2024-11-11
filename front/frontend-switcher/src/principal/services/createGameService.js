// createGameService.js: Servicio para crear una partida
import URL_API from "../../configs/urlAPI";

export const createGameService = async (gameData) => {
  try {
    const response = await fetch(URL_API + "/home/crear", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(gameData),
    });

    if (!response.ok) {
      throw new Error("Error al crear la partida");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error:", error);
    throw error;
  }
};
