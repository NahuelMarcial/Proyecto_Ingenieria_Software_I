import React from "react";
import { render, fireEvent } from "@testing-library/react";
import SwitchDifficulty from "../principal/components/SwitchDifficulty";

describe("Describe SwitchDifficulty:", () => {
  it("se deberia renderizar correctamente.", () => {
    const { getByText } = render(<SwitchDifficulty />);
    expect(getByText("Dificultad")).toBeInTheDocument();
    expect(getByText("Difícil")).toBeInTheDocument();
    expect(getByText("Fácil")).toBeInTheDocument();
  });

  it("deberia cambiar la dificultad al hacer click en el boton.", () => {
    const { getByRole, getByText } = render(<SwitchDifficulty />);
    const button = getByRole("button");

    // Initial state should be easy
    expect(button).toHaveStyle("margin-left: 0");
    expect(getByText("Fácil")).toBeInTheDocument();
    expect(button.querySelector("svg")).toHaveAttribute(
      "data-testid",
      "HappyFaceIcon"
    );

    // Click to switch to difficult
    fireEvent.click(button);
    expect(button).toHaveStyle("margin-left: 50%");
    expect(getByText("Difícil")).toBeInTheDocument();
    expect(button.querySelector("svg")).toHaveAttribute(
      "data-testid",
      "AngryFaceIcon"
    );

    // Click to switch back to easy
    fireEvent.click(button);
    expect(button).toHaveStyle("margin-left: 0");
    expect(getByText("Fácil")).toBeInTheDocument();
    expect(button.querySelector("svg")).toHaveAttribute(
      "data-testid",
      "HappyFaceIcon"
    );
  });
});
