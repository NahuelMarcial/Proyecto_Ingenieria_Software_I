import URL_API from "../../configs/urlAPI";

const startGame = async (gameid, playerid) => {
  const body = { jugador: playerid };
  try {
    const response = await fetch(URL_API + "/lobby/" + gameid + "/iniciar/", {
      method: "PATCH",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (response.ok !== true) {
      throw new Error("No se pudo iniciar la partida");
    }
    console.log("Partida", gameid, "iniciada...");
    let isstarted = await response.json();
    return isstarted.iniciada;
  } catch (e) {
    console.log("Error", e);
    throw e;
  }
};

export default startGame;
