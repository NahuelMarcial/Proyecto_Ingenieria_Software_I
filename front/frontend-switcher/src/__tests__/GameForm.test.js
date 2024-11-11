import React from "react";
import { render, fireEvent, screen } from "@testing-library/react";
import GameForm from "../principal/components/GameForm";

describe("GameForm", () => {
  let formData;
  let onInputChange;
  let onSubmit;
  let loading;

  beforeEach(() => {
    formData = { nombre: "JuegoDePrueba", max_jugadores: "4" };
    onInputChange = jest.fn();
    onSubmit = jest.fn((e) => {
      e.preventDefault();
    });
    loading = false;
  });

  test("se renderiza correctamente", () => {
    const { getByLabelText, getByRole } = render(
      <GameForm
        formData={formData}
        onInputChange={onInputChange}
        onSubmit={onSubmit}
        loading={loading}
      />
    );

    expect(screen.getByTestId("title-name-game-form")).toBeInTheDocument();
    expect(screen.getByTestId("title-max-players")).toBeInTheDocument();
    expect(getByRole("button", { name: /Crear/i })).toBeInTheDocument();
  });

  test("llama a onSubmit con los datos del formulario al enviar", () => {
    const { getByLabelText, getByRole } = render(
      <GameForm
        formData={{ nombre: "Juego de Prueba", max_jugadores: 4 }}
        onInputChange={onInputChange}
        onSubmit={onSubmit}
        loading={loading}
      />
    );

    fireEvent.submit(getByRole("button", { name: /Crear/i }));
    expect(onSubmit).toHaveBeenCalled();
  });

  test("desactiva el botón cuando loading es true", () => {
    loading = true;
    const { getByRole } = render(
      <GameForm
        formData={formData}
        onInputChange={onInputChange}
        onSubmit={onSubmit}
        loading={loading}
      />
    );

    expect(getByRole("button", { name: /Creando.../i })).toBeDisabled();
  });
});
