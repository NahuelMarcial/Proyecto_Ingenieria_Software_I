import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import CreateGameButton from "../principal/components/CreateGameButton";

// Test para verificar que el botón se renderiza correctamente
test("debería renderizar el botón con el texto CREAR PARTIDA", () => {
  render(<CreateGameButton />);
  const buttonElement = screen.getByText("CREAR PARTIDA");
  expect(buttonElement).toBeInTheDocument();
});

// Test para verificar que la función onClick se llama al hacer clic
test("debería llamar la función onClick cuando se hace clic", () => {
  const handleClick = jest.fn(); // mock de la función onClick
  render(<CreateGameButton onClick={handleClick} />);

  const buttonElement = screen.getByText("CREAR PARTIDA");
  fireEvent.click(buttonElement); // Simula el clic en el botón

  expect(handleClick).toHaveBeenCalledTimes(1); // Verifica si se llamó la función
});
