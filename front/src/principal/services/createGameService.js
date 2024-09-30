// createGameService.js: Servicio para crear una partida

const API_URL = "https://proyecto-ingenieria-software-i.onrender.com/partida/crear";

export const createGameService = async (gameData) => {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(gameData),
    });

    console.log("Response:", response.body);
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
