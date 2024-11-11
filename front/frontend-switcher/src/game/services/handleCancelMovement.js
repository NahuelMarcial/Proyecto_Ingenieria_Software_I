import emitter from "./eventEmitter";
import CancelMovementservice from "./CancelMovement";

let ishandlecancel = false;

const handleCancelMovement = () => {
	if (ishandlecancel) {
		return;
	}
	ishandlecancel = true;
	const cancelMovementListener = async (jugador_id) => {
		const partida_id = Number(sessionStorage.getItem("partida_id"));
		console.log("Partida ", partida_id);
		console.log("jugador ", jugador_id);

		await CancelMovementservice(partida_id, jugador_id)
	};

	emitter.on("CancelMovement", cancelMovementListener);
	return () => {
		emitter.off("CancelMovement", cancelMovementListener);
	};
};

export default handleCancelMovement;