import URL_API from "../../configs/urlAPI";

// Función para crear fichas
export const newSetFichas = async (partida_id) => {
  const response = await fetch(URL_API + `/game/${partida_id}/fichas/crear`, {
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
