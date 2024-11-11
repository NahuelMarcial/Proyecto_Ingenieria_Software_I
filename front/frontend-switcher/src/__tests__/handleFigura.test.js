// handleMovement.test.js
import emitter from "../game/services/eventEmitter";
import usarFigura from "../game/services/usarFigura";
import handleFigura from "../game/services/handleFigura";

// Mockear el módulo 'usarMovimiento' para controlar su comportamiento en los tests
jest.mock("../game/services/usarFigura", () => jest.fn());

describe("handleFigura", () => {
  let emittedEvents; //Array para guardar los eventos emitidos
  let turnOffListeners;

  beforeEach(() => {
    emittedEvents = [];
    handleFigura(); // obtenemos la función para apagar los listeners
    usarFigura.mockReset();
    // Agregar un listener para rastrear los eventos emitidos
    emitter.on("figCardSelected", () => emittedEvents.push("figCardSelected"));
    emitter.on("tileSelectedAfterFig", () =>
      emittedEvents.push("tileSelectedAfterFig")
    );
  });

  afterEach(() => {
    jest.clearAllMocks(); // Limpiar los mocks después de cada test
    emitter.off("figCardSelected");
    emitter.off("tileSelectedAfterFig");
  });

  it("Debería seleccionar una carta y una ficha correctamente siguiendo el orden", async () => {
    console.log("~~~~~~ TEST 1 ~~~~~~");
    emitter.emit("testseter", "");
    usarFigura.mockImplementation((card, tile) => {
      if (card !== null && tile !== null) {
        console.log("Se seleccionó correctamente una carta y una ficha");
        return Promise.resolve({status: 200});
      }
      return Promise.resolve({status: 400});
    });

    console.log("Seleccionando Carta figura...");
    emitter.emit("figCardSelected", 1);

    console.log("Seleccionando Ficha...");
    emitter.emit("tileSelectedAfterFig", "ficha1");

    await expect(emittedEvents).toEqual([
      "figCardSelected",
      "tileSelectedAfterFig",
    ]);

    await expect(usarFigura).toHaveBeenCalledWith(1, "ficha1");

    console.log("TEST 1 TERMINADO");
  });

  it("Si se selecciona una carta figura despues de otra, se debe ejecutar esta ultima", async () => {
    console.log("~~~~~~ TEST 2 ~~~~~~");
    emitter.emit("testseter", "");

    usarFigura.mockImplementation((card, tile) => {
      if (card !== null && tile !== null) {
        console.log(`Se seleccionó la carta figura ${card} y la ficha ${tile}`);
        return Promise.resolve({status: 200});
      }
      return Promise.resolve({status: 400});
    });

    // Emite el primer evento seleccionando la primera carta figura
    console.log("Seleccionando primera carta figura...");
    emitter.emit("figCardSelected", 1); // Seleccionar la primera carta figura

    // Ahora seleccionamos la segunda carta figura
    console.log("Seleccionando segunda carta figura...");
    emitter.emit("figCardSelected", 2); // Seleccionar la segunda carta figura

    // Emitir la selección de ficha después de la segunda carta
    console.log("Seleccionando Ficha...");
    emitter.emit("tileSelectedAfterFig", "ficha1");

    // Asegurarnos de que la segunda carta es la que se usó
    await expect(usarFigura).toHaveBeenCalledWith(2, "ficha1");

    // Verificar que no se llamó usarFigura con la primera carta
    await expect(usarFigura).not.toHaveBeenCalledWith(1, "ficha1");
    console.log("Se ejecutó correctamente la carta 2, a pesar de antes haberse seleccionado la carta 1 anteriormente");
  });

  it("Si se juega una carta figura con una ficha no perteneciente a una figura, se debe cancelar la selección de esta carta", async () => {
    console.log("~~~~~~ TEST 3 ~~~~~~");
    emitter.emit("testseter", "");
    // Mock de usarFigura que simula que la ficha no es válida
    usarFigura.mockImplementation((card, tile) => {
      console.log(
        `Intento de usar la carta figura ${card} con la ficha ${tile}`
      );

      // Simular que la ficha no pertenece a una figura
      return Promise.resolve({status: 400});
    });

    let figCanceladoEmitted = false;

    // Listener para detectar la cancelación de la selección de carta figura
    emitter.on("figCancelado", () => {
      figCanceladoEmitted = true;
    });

    // Seleccionar la carta figura
    console.log("Seleccionando carta figura...");
    emitter.emit("figCardSelected", 1);

    // Seleccionar una ficha que no pertenece a una figura
    console.log("Seleccionando ficha no válida...");
    emitter.emit("tileSelectedAfterFig", "fichaInvalida");

    // Verificar que se llamó a usarFigura con la carta y ficha incorrectas
    await expect(usarFigura).toHaveBeenCalledWith(1, "fichaInvalida");

    // Verificar que se emitió el evento de cancelación
    await expect(figCanceladoEmitted).toBe(true);

    console.log(
      "Se emitió correctamente el evento de cancelación al usar una ficha no válida."
    );
  });

});
