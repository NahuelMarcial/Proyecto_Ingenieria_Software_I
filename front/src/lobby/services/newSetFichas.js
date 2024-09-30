const API_URL = "https://proyecto-ingenieria-software-i.onrender.com/fichas/crear/";

// Función para crear fichas
export const newSetFichas = async (partida_id) => {
  const response = await fetch(API_URL + partida_id, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Error al crear las fichas");
  }

  return await response.json(); // Devuelve las fichas creadas
};

export default newSetFichas;
