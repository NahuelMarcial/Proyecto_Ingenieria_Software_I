import URL_API from "../../configs/urlAPI";

const cheatDescartarService = async (partida_id, id_player) => {
  try {
    const body = { 
      id_player: id_player 
    };
    const response = await fetch(
      URL_API + `/game/${partida_id}/carta_figura/cheat_descartar`,
      {
        method: "PATCH",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      }
    );

    if (!response.ok) {
      throw new Error("Error al activar cheat de descartar cartas");
    }

    const data = await response.json();
    return data; // Puedes manejar la respuesta como necesites
  } catch (error) {
    console.error("Error en cheatDescartarService:", error);
    throw error;
  }
};

export default cheatDescartarService;
