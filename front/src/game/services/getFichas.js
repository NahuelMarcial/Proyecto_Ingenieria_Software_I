const API_URL = "https://proyecto-ingenieria-software-i.onrender.com/fichas/listar/";

// Función para obtener fichas
export const getFichas = async (partida_id) => {
  const response = await fetch(API_URL + partida_id, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Error al obtener las fichas");
  }

  return await response.json();
};

export default getFichas;
