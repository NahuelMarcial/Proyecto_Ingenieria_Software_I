import React from "react";
import { render, screen, waitFor, act } from "@testing-library/react";
import GameList from "../principal/containers/GameList";
import { getGameListServices } from "../principal/services/getGameListServices";
import { MemoryRouter } from "react-router-dom";

// Mock del servicio
jest.mock("../principal/services/getGameListServices");

// Mock del socket
const mockSocket = {
  on: jest.fn(),
  off: jest.fn(),
};

describe("GameList", () => {
  beforeEach(() => {
    jest.clearAllMocks(); // Limpia los mocks antes de cada test
  });

  test("renderiza correctamente sin partidas disponibles", async () => {
    // Simula que el servicio retorna una lista vacía
    getGameListServices.mockResolvedValue([]);
    await act(async () => {
      render(
        <MemoryRouter>
          <GameList socket={mockSocket} />
        </MemoryRouter>
      );
    });
    // Verifica que el texto "No hay mesas disponibles todavía..." aparece
    expect(
      screen.getByText(/No hay mesas disponibles todavía/i)
    ).toBeInTheDocument();
  });

  test("renderiza la lista de partidas disponibles", async () => {
    // Simula que el servicio retorna algunas partidas
    const mockGames = [
      { id: "1", nombre: "Partida 1", cantidad_jugadores: 2, max_jugadores: 4 },
      { id: "2", nombre: "Partida 2", cantidad_jugadores: 3, max_jugadores: 4 },
    ];
    getGameListServices.mockResolvedValue(mockGames);
    await act(async () => {
      render(
        <MemoryRouter>
          <GameList socket={mockSocket} />
        </MemoryRouter>
      );
    });
    // Espera a que las partidas se rendericen
    await waitFor(() => {
      expect(screen.getByText("Partida 1")).toBeInTheDocument();
      expect(screen.getByText("Partida 2")).toBeInTheDocument();
    });
  });

  test("llama a getGameListServices al montar el componente", async () => {
    getGameListServices.mockResolvedValue([]);
    await act(async () => {
      render(
        <MemoryRouter>
          <GameList socket={mockSocket} />
        </MemoryRouter>
      );
    });
    // Verifica que getGameListServices fue llamado una vez
    await waitFor(() => {
      expect(getGameListServices).toHaveBeenCalledTimes(1);
    });
  });

  test("actualiza la lista cuando se recibe el evento 'partida_creada'", async () => {
    const mockGames = [
      { id: "1", nombre: "Partida 1", cantidad_jugadores: 2, max_jugadores: 4 },
    ];
    getGameListServices.mockResolvedValue(mockGames);
    await act(async () => {
      render(
        <MemoryRouter>
          <GameList socket={mockSocket} />
        </MemoryRouter>
      );
    });
    // Simula que el evento "partida_creada" se dispara
    await waitFor(() => {
      expect(mockSocket.on).toHaveBeenCalledWith(
        "partida_creada",
        expect.any(Function)
      );
    });
  });

  test("limpia los eventos de socket al desmontar", async () => {
    const { unmount } = render(
      <MemoryRouter>
        <GameList socket={mockSocket} />
      </MemoryRouter>
    );
    unmount();
    expect(mockSocket.off).toHaveBeenCalledWith("partida_creada");
    expect(mockSocket.off).toHaveBeenCalledWith("jugador_unido");
  });
});
