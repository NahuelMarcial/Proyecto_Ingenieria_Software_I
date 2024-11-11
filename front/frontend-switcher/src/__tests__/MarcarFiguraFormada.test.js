import React from "react";
import { render, screen, waitFor } from "@testing-library/react";
import Tablero from "../game/containers/Tablero";
import getFichas from "../game/services/getFichas";
import getMarkedFigs from "../game/services/getMarkedFigs";

// Mock del servicio getFichas
jest.mock("../game/services/getFichas");

// Mock del servicio getMarkedFigs
jest.mock("../game/services/getMarkedFigs");

describe("Tablero con figuras formadas", () => {
  const mockSocket = {
    on: jest.fn(),
    off: jest.fn(),
  };

  const partida_id = "123";

  beforeEach(() => {
    jest.clearAllMocks();
    sessionStorage.setItem("partida_id", partida_id);
  });

  test("resalta las fichas que forman una figura como 'fige1_n' después de un movimiento", async () => {
    // Mockear las fichas obtenidas del servicio
    getFichas.mockResolvedValue([
      { pos_x: 1, pos_y: 6, color: "azul" },
      { pos_x: 2, pos_y: 6, color: "azul" },
      { pos_x: 2, pos_y: 5, color: "azul" },
      { pos_x: 3, pos_y: 5, color: "azul" },
      { pos_x: 3, pos_y: 4, color: "rojo" }, // Una ficha extra que no forma parte de la figura
    ]);

    // Mockear las figuras formadas obtenidas del servicio
    getMarkedFigs.mockResolvedValue([
      {
        fichas: [
          // Coordenadas de la figura fige1_n
          [
            [1, 6],
            [2, 6],
            [2, 5],
            [3, 5],
          ],
        ],
      },
    ]);

    render(<Tablero socket={mockSocket} />);

    // Simular que el socket dispara el evento "set_fichas_creado"
    await waitFor(() => {
      mockSocket.on.mock.calls[0][1](); // Ejecuta el callback del evento
    });

    // Verificar que las fichas se renderizaron correctamente
    expect(screen.getAllByTestId(/^ficha-/)).toHaveLength(5); // Hay 5 fichas en total

    // Verificar que las fichas que forman la figura están resaltadas (borde blanco)
    const ficha1_6 = screen.getByTestId("ficha-1-6");
    expect(ficha1_6).toHaveStyle("border: 4px solid orange");
    expect(ficha1_6).toHaveStyle("background-color: rgb(0, 173, 238)");

    const ficha2_6 = screen.getByTestId("ficha-2-6");
    expect(ficha2_6).toHaveStyle("border: 4px solid orange");
    expect(ficha2_6).toHaveStyle("background-color: rgb(0, 173, 238)");

    const ficha2_5 = screen.getByTestId("ficha-2-5");
    expect(ficha2_5).toHaveStyle("border: 4px solid orange");
    expect(ficha2_5).toHaveStyle("background-color: rgb(0, 173, 238)");

    const ficha3_5 = screen.getByTestId("ficha-3-5");
    expect(ficha3_5).toHaveStyle("border: 4px solid orange");
    expect(ficha3_5).toHaveStyle("background-color: rgb(0, 173, 238)");

    // Verificar que una ficha que no forma parte de la figura no tiene borde blanco
    const ficha3_4 = screen.getByTestId("ficha-3-4");
    expect(ficha3_4).toHaveStyle("border: 4px solid orange");
    expect(ficha3_4).toHaveStyle("background-color: rgb(236, 28, 36)");
  });
});
