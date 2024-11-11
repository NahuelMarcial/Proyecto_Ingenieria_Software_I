import emitter from "../game/services/eventEmitter";
import usarMovimiento from "../game/services/usarMovimiento";
import handleMovement from "../game/services/handleMovement";
import getMovPossible from "../game/services/getMovPossible";

// Mockear los módulos 'usarMovimiento' y 'getMovPossible'
jest.mock("../game/services/usarMovimiento", () => jest.fn());
jest.mock("../game/services/getMovPossible", () => jest.fn());

describe("handleMovement", () => {
  let emittedEvents;

  beforeEach(() => {
    emittedEvents = [];
    handleMovement();
    usarMovimiento.mockReset();
    getMovPossible.mockReset();

    emitter.on("movCardSelected", () => emittedEvents.push("movCardSelected"));
    emitter.on("tileSelectedAfterMov", () =>
      emittedEvents.push("tileSelectedAfterMov")
    );
  });

  afterEach(() => {
    jest.clearAllMocks();
    emitter.off("movCardSelected");
    emitter.off("tileSelectedAfterMov");
  });

  it("debería seleccionar una carta y emitir posibles movimientos al seleccionar la primera ficha", async () => {
    // Mockear la respuesta de 'getMovPossible'
    getMovPossible.mockResolvedValue(["ficha2", "ficha3"]);

    // Espiar el evento 'emit' del emitter antes de emitir los eventos simulados
    const firstTileSelectedSpy = jest.spyOn(emitter, "emit");

    // Emitir eventos simulados
    emitter.emit("movCardSelected", 1); // Seleccionar una carta
    await emitter.emit("tileSelectedAfterMov", "ficha1"); // Seleccionar la primera ficha

    // Esperar que getMovPossible sea llamada con los argumentos correctos
    expect(getMovPossible).toHaveBeenCalledWith(1, "ficha1");

    // Verificar que el evento 'firstTileSelected' fue emitido con las posibles fichas
    expect(firstTileSelectedSpy).toHaveBeenCalledWith("firstTileSelected", [
      "ficha2",
      "ficha3",
    ]);
  });
});
