import URL_API from "../../configs/urlAPI";

const createName = async (name) => {
  const jugador_id = sessionStorage.getItem("jugador_id");
  const sid = sessionStorage.getItem("sid");
  const body = { player_id: jugador_id, nombre: name, sid: sid };

  try {
    const response = await fetch(`${URL_API}/home/asignar_nombre`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!response) {
      throw new Error("Error al asignar el nombre");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.log("Error: createName", error);
    throw error;
  }
};

export default createName;
