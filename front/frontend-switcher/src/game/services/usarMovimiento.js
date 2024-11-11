import URL_API from "../../configs/urlAPI";
import emitter from "./eventEmitter";

const usarMovimiento = async (id_carta, id_ficha1, id_ficha2) => {
  const partida_id = sessionStorage.getItem("partida_id");
  const id_jugador = sessionStorage.getItem("jugador_id");

  try {
    const response = await fetch(
      URL_API + `/game/${partida_id}/carta_movimiento/usar_carta_movimiento`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id_carta: id_carta,
          id_jugador: id_jugador,
          id_ficha1: id_ficha1,
          id_ficha2: id_ficha2,
        }),
      }
    );
    if (!response) {
      throw new Error("No se pudo usar el movimiento");
    }

    const data = await response.json();
    if (response.ok) {
      emitter.emit("log_MovimientoParcialRealizado", id_jugador);
    }
    return data;
  } catch (error) {
    console.error("Error: usarMovimiento.");
    throw error;
  }
};

export default usarMovimiento;
