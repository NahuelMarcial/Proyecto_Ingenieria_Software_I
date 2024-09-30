const API_startgame = "http://localhost:8000/lobby/iniciar/";

const startGame = async (gameid, playerid) => {
  const body = { jugador: playerid };
  try {
    const response = await fetch(API_startgame + gameid, {
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
    let isstarted = await response.json();
    return isstarted.iniciada;
  } catch (e) {
    console.log("Error", e);
    throw e;
  }
};

export default startGame;
