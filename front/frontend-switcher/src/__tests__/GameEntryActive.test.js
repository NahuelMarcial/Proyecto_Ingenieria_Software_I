// GameEntryActive.test.jsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import GameEntryActive from "../principal/components/GameEntryActive";

describe("GameEntryActive Component", () => {
  const defaultProps = {
    gameId: "123",
    gameName: "Test Game",
    gameState: 1, // Estado de "En espera"
    isMyTurn: true,
    isIniciada: false,
  };

  const renderWithRouter = (ui, options) => {
    return render(ui, { wrapper: MemoryRouter, ...options });
  };

  test("renders game name", () => {
    renderWithRouter(<GameEntryActive {...defaultProps} />);
    expect(screen.getByText(/Test Game/i)).toBeInTheDocument();
  });

  test("renders IsMyTurn when it is my turn and game is not finished", () => {
    renderWithRouter(<GameEntryActive {...defaultProps} />);
    expect(screen.getByText(/¡Tu turno!/i)).toBeInTheDocument();
  });

  test("renders GameState component", () => {
    renderWithRouter(<GameEntryActive {...defaultProps} />);
    expect(screen.getByTestId("game-state")).toBeInTheDocument();
  });
});
