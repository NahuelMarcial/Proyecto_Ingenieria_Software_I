import emitter from "./eventEmitter";
import blockCardService from "./BlockCardService";

let selectedCard = null;
let selectedTile = null;
let isUsedBlock = false;
const handleFiguraBlock = () => {
  if (isUsedBlock) {
    return;
  }
  isUsedBlock = true;

  const figCardSelectedForBlockListener = (card) => {
    selectedCard = card;
    selectedTile = null;
    console.log("Carta seleccionada para bloquear:", selectedCard);
  };

  const tileSelectedAfterFigListener = async (tile) => {
    const partida_id = sessionStorage.getItem("partida_id");
    const jugador_id = sessionStorage.getItem("jugador_id");

    if (selectedCard !== null) {
      selectedTile = tile;
      try {
        const response = await blockCardService(
          partida_id,
          jugador_id,
          selectedCard,
          selectedTile
        );
        console.log("respuesta", response);
        console.log(
          "Blockeo exitoso con carta y ficha:",
          selectedCard,
          selectedTile,
          "del jugador:",
          jugador_id
        );
        resetSelection();
      } finally {
        emitter.emit("figCancelado", false);
      }
    }
  };
  const testseter = () => {
    isUsedBlock = false;
    console.log("Seter test: ", isUsedBlock);
  };

  // Registrar los listeners
  emitter.on("figCardSelectedForBlock", figCardSelectedForBlockListener);
  emitter.on("testseter", testseter);
  emitter.on("tileSelectedAfterFig", tileSelectedAfterFigListener);

  const resetSelection = () => {
    selectedCard = null;
    selectedTile = null;
  };

  return () => {
    emitter.off("figCardSelectedForBlock", figCardSelectedForBlockListener);
    emitter.off("tileSelectedAfterFig", tileSelectedAfterFigListener);
    emitter.off("testseter", testseter);
  };
};

export default handleFiguraBlock;
