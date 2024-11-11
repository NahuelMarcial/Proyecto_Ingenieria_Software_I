import React from "react";
import { render, screen } from "@testing-library/react";
import PlayerList from "../lobby/components/PlayerList";

// Mock del componente PlayerCard
jest.mock(
  "../lobby/components/PlayerCard.jsx",
  () =>
    ({ player, name, face }) =>
      (
        <div data-testid="player-card">
          <span>{player ? `Player: ${name}` : "Disponible"}</span>
          <span>Face: {face}</span>
        </div>
      )
);

describe("PlayerList", () => {
  const playersMock = {
    jugador1: true,
    jugador2: true,
    jugador3: false,
    jugador4: false,
  };

  const playersNamesMock = {
    jugador1: "Alice",
    jugador2: "Bob",
    jugador3: "Disponible",
    jugador4: "Disponible",
  };

  test("debería renderizar el número correcto de PlayerCards basado en maxPlayers", () => {
    const maxPlayers = 3;

    render(
      <PlayerList
        players={playersMock}
        playersNames={playersNamesMock}
        maxPlayers={maxPlayers}
      />
    );

    const playerCards = screen.getAllByTestId("player-card");
    expect(playerCards).toHaveLength(maxPlayers);
  });

  test("debería mostrar 'Disponible' cuando no hay jugador en la posición", () => {
    render(
      <PlayerList
        players={playersMock}
        playersNames={playersNamesMock}
        maxPlayers={4}
      />
    );

    const availableSlots = screen.getAllByText("Disponible");
    expect(availableSlots).toHaveLength(2); // Jugador3 y Jugador4 están disponibles
  });

  test("debería mostrar los nombres correctos de los jugadores", () => {
    render(
      <PlayerList
        players={playersMock}
        playersNames={playersNamesMock}
        maxPlayers={4}
      />
    );

    expect(screen.getByText("Player: Alice")).toBeInTheDocument();
    expect(screen.getByText("Player: Bob")).toBeInTheDocument();
  });
});
