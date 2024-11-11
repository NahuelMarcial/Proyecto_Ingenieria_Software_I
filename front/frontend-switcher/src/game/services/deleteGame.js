import URL_API from "../../configs/urlAPI";

const deleteGame = async (partida_id, sid) => {
  try {
    const response = await fetch(
      URL_API + `/game/${partida_id}/eliminar/${sid}`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    if (!response.ok) {
      throw new Error("No se pudo eliminar la partida");
    }
    return response;
  } catch (e) {
    throw e;
  }
};

export default deleteGame;
