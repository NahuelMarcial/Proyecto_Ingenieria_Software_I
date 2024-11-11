import React from "react";
import { render, screen } from "@testing-library/react";
import NotAvailableGames from "../principal/components/NotAvailableGames";
import "@testing-library/jest-dom";

describe("NotAvailableGames Component", () => {
  test("debería mostrar el texto 'No hay Partidas, pero no se encuentra.'", () => {
    render(<NotAvailableGames />);
    const textElement = screen.getByText(/No hay Partidas./i);
    expect(textElement).toBeInTheDocument();
  });

  test("debería mostrar un ícono de carita triste, pero no se encuentra.", () => {
    render(<NotAvailableGames />);
    const iconElement = screen.getByTestId("SentimentVeryDissatisfiedIcon");
    expect(iconElement).toBeInTheDocument();
  });
});
