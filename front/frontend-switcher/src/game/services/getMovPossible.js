import URL_API from "../../configs/urlAPI";

const getMovPossible = async (id_carta, id_ficha) => {
  const partida_id = sessionStorage.getItem("partida_id");

  try {
    const response = await fetch(
      `${URL_API}/game/${partida_id}/carta_movimiento/get_movimientos_posibles/${id_carta}/${id_ficha}`
    );

    if (!response.ok) {
      throw new Error("Error al obtener los posibles movimientos de ficha.");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error en getMovPossible", error);
    throw error;
  }
};

export default getMovPossible;
