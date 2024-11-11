import URL_API from "../../configs/urlAPI";
import emitter from "./eventEmitter";

const usarFigura = async (id_carta, id_ficha) => {
  const partida_id = sessionStorage.getItem("partida_id");
  const id_player = sessionStorage.getItem("jugador_id");

  try {
    const response = await fetch(
      URL_API + `/game/${partida_id}/carta_figura/jugar_carta`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id_carta: id_carta,
          id_ficha: id_ficha,
          id_player: id_player,
        }),
      }
    );
    if (!response.ok) {
      throw new Error("No se pudo jugar la carta figura");
    }

    const data = await response.json();
    if (response.ok) {
      emitter.emit("log_FiguraRealizada", id_player);
    }
    return data;
  } catch (error) {
    console.error("Error: usarFigura.");
    throw error;
  }
};

export default usarFigura;
