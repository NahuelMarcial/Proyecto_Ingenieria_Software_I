import URL_API from "../../configs/urlAPI";

export const getMarkedFigs = async (partida_id) => {
  const response = await fetch(
    URL_API + `/game/${partida_id}/fichas/buscar_figuras_formadas`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }
  );

  if (!response.ok) {
    throw new Error("Error al obtener las figuras formadas");
  }

  return await response.json();
};

export default getMarkedFigs;
