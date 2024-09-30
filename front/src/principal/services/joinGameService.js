// joinGameService.js: Servicio para unirse a una partida

const joinGameService = async (partida_id) => {
  const jugador = sessionStorage.getItem("jugador_id");
  const sid = sessionStorage.getItem("sid");

  console.log("Datos enviados:", partida_id, jugador, sid);
  const url = `https://proyecto-ingenieria-software-i.onrender.com/partida/unirse/${partida_id}`;

  try {
    const response = await fetch(url, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        jugador: jugador,
        sid: sid,
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
