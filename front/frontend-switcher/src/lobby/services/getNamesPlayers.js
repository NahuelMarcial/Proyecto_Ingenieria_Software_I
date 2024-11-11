import URL_API from "../../configs/urlAPI";

const getNamesPlayers = async (partida_id) => {
  try {
    const response = await fetch(`${URL_API}/lobby/${partida_id}/nombres`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response) {
      throw new Error("Error al obtener los nombres");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.log("Error: getNamesPlayers", error);
    throw error;
  }
};

export default getNamesPlayers;
