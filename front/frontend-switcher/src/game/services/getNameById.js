import URL_API from "../../configs/urlAPI";

const getNameById = async (id) => {
  try {
    const response = await fetch(`${URL_API}/home/nombre_jugador/${id}`);

    if (!response.ok) {
      throw new Error("Error en la petición");
    }

    const data = await response.json();
    return data.nombre;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export default getNameById;
