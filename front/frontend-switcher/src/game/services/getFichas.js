import URL_API from "../../configs/urlAPI";

export const getFichas = async (partida_id) => {
  const response = await fetch(URL_API + `/game/${partida_id}/fichas/listar`, {
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
