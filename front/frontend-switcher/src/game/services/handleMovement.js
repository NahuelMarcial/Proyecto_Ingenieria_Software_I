import emitter from "./eventEmitter";
import usarMovimiento from "./usarMovimiento";
import getMovPossible from "./getMovPossible";

let isListenerRegistered = false;

const handleMovement = async () => {
  if (isListenerRegistered) return;
  isListenerRegistered = true;

  let selectedCard = null;
  let selectedTiles = [];

  const movCardSelectedListener = (card_id) => {
    selectedTiles = [];
    selectedCard = card_id;
  };

  const tileSelectedMovListener = async (tileId) => {
    if (selectedTiles.length < 2 && selectedCard) {
      selectedTiles.push(tileId);

      if (selectedTiles.length === 1) {
        // Fetch de posibles movimientos tras seleccionar la primera ficha
        const possibleTiles = await getMovPossible(selectedCard, tileId);
        emitter.emit("firstTileSelected", possibleTiles);
        console.log("Posibles movimientos:", possibleTiles);
      } else if (selectedTiles.length === 2) {
        // Si ya hay dos fichas seleccionadas, hacer el fetch
        await usarMovimiento(selectedCard, selectedTiles[0], selectedTiles[1])
          .then((response) => {
            resetSelection();
            if (response.status !== 200) {
              emitter.emit("movCancelado", false);
            }
            emitter.emit("movCompleted");
          })
          .catch((error) => {
            console.error("Error al realizar el movimiento:", error);
          });
      }
    }
  };

  // Registrar los listeners
  emitter.on("movCardSelected", movCardSelectedListener);
  emitter.on("tileSelectedAfterMov", tileSelectedMovListener);

  // Resetear selección después de ejecutar el movimiento
  const resetSelection = () => {
    selectedCard = null;
    selectedTiles = [];
  };

  // Limpiar los listeners al terminar o cuando ya no sean necesarios
  return () => {
    emitter.off("movCardSelected", movCardSelectedListener);
    emitter.off("tileSelectedAfterMov", tileSelectedMovListener);
  };
};

export default handleMovement;
