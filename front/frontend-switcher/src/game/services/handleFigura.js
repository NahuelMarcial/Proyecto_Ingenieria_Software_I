import emitter from "./eventEmitter";
import usarFigura from "./usarFigura";

let selectedCard = null;
let selectedTile = null;
let isUsedFigure = false;
const handleFigura = () => {
  if (isUsedFigure) {
    return;
  }
  isUsedFigure = true;
  // Definir las funciones de callback
  const figCardSelectedListener = (card) => {
    selectedCard = card; // Cambiar la carta seleccionada
    selectedTile = null; // Resetear la ficha seleccionada
    console.log("Carta seleccionada para usar figura:", selectedCard);
  };

  const tileSelectedAfterFigListener = async (tile) => {
    if (selectedCard !== null) {
      selectedTile = tile;
      try {
        console.log(
          "Movimiento con carta y ficha:",
          selectedCard,
          selectedTile
        );
        const response = await usarFigura(selectedCard, selectedTile);
        console.log(
          "Movimiento exitoso con carta y ficha:",
          selectedCard,
          selectedTile
        );
        if (response.status !== 200) {
          emitter.emit("figCancelado", false);
        }
        resetSelection();
      } catch (error) {
        console.error("Error al realizar el movimiento:", error);
      }
    }
  };
  const testseter = () => {
    isUsedFigure = false;
    console.log("Seter test: ", isUsedFigure);
  };

  // Registrar los listeners
  emitter.on("figCardSelected", figCardSelectedListener);
  emitter.on("testseter", testseter);
  emitter.on("tileSelectedAfterFig", tileSelectedAfterFigListener);

  const resetSelection = () => {
    selectedCard = null;
    selectedTile = null;
  };

  // Retornar una función para apagar los listeners
  return () => {
    emitter.off("figCardSelected", figCardSelectedListener);
    emitter.off("tileSelectedAfterFig", tileSelectedAfterFigListener);
    emitter.off("testseter", testseter);
  };
};

export default handleFigura;
