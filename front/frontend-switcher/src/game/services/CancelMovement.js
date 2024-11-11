import URL_API from "../../configs/urlAPI";
import emitter from "./eventEmitter";

const CancelMovementservice = async (partida_id, id_player) => {
  try {
    const body = {
      id_player: id_player,
    };
    const response = await fetch(
      URL_API + `/game/${partida_id}/carta_movimiento/deshacer_movimiento`,
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
      throw new Error("Error al cancelar movimiento");
    }
    if (response.ok) {
      emitter.emit("log_MovimientoParcialCancelado", id_player);
    }
  } catch (e) {
    console.log("Error al cancelar movimiento parcial");
    throw e;
  }
};

export default CancelMovementservice;
