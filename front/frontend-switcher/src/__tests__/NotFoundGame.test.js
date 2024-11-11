import React from "react";
import { render, screen } from "@testing-library/react";
import NotFoundGames from "../principal/components/NotFoundGames";
import "@testing-library/jest-dom";

describe("NotFoundGames Component", () => {
  test("debería mostrar el texto 'Sin Coincidencia...', pero no se muestra.'", () => {
    render(<NotFoundGames />);
    const textElement = screen.getByText(/sin coincidencia.../i);
    expect(textElement).toBeInTheDocument();
  });

  test("debería mostrar el icono de interrogacion, pero no se muestra.", () => {
    render(<NotFoundGames />);
    const iconElement = screen.getByTestId("HelpOutlineIcon");
    expect(iconElement).toBeInTheDocument();
  });
});
