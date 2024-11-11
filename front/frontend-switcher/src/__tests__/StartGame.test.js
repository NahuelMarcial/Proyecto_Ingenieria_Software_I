import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import StartGameButton from "../lobby/components/StartGameButton";

describe("Start game tests", () => {
  test("Render button", () => {
    const fun = jest.fn();
    render(<StartGameButton onClick={fun} />);
    const button = screen.getByText("Iniciar Juego");
    expect(button).toBeInTheDocument();
  });
  test("onclick work owner", () => {
    const fun = jest.fn();
    render(<StartGameButton isOwner={true} onClick={fun} isAvailable={true} />);
    const button = screen.getByText("Iniciar Juego");
    fireEvent.click(button);
    expect(fun).toHaveBeenCalled();
  });
  test("onclick work not owner", () => {
    const fun = jest.fn();
    render(<StartGameButton isOwner={false} onClick={fun} />);
    const button = screen.getByText("Iniciar Juego");
    fireEvent.click(button);
    expect(fun).not.toHaveBeenCalled();
  });
});
