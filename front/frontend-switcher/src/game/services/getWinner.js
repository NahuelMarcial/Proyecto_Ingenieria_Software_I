import URL_API from "../../configs/urlAPI";

export const getWinner = async (partida_id) => {
  const response = await fetch(URL_API + `/game/${partida_id}/ganador`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Error al obtener el ganador");
  }

  return await response.json();
};

export default getWinner;
