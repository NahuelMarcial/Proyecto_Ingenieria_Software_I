// joinGameService.js: Servicio para unirse a una partida
import URL_API from "../../configs/urlAPI";

const joinGameService = async (partida_id, password) => {
  const jugador = sessionStorage.getItem("jugador_id");
  const sid = sessionStorage.getItem("sid");
  const url = URL_API + `/home/unirse/${partida_id}`;

  try {
    const response = await fetch(url, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        jugador: jugador,
        sid: sid,
        password: password, // Por defecto no tiene contraseña
      }),
    });

    if (!response.ok) {
      throw new Error("Error al unirse a la partida");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error en joinGameService:", error);
    throw error;
  }
};

export default joinGameService;
