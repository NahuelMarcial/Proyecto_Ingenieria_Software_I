import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import SetNickname from "../principal/components/CreateUserName.jsx";
import createName from "../principal/services/createName";

// Mock de la función createName
jest.mock("../principal/services/createName", () => jest.fn());

describe("SetNickname Component", () => {
  beforeEach(() => {
    sessionStorage.clear(); // Limpiar el sessionStorage antes de cada test
  });

  it("debería mostrar el diálogo si no hay un nombre de jugador en sessionStorage", () => {
    render(<SetNickname />);

    // Verificar que el diálogo está abierto
    expect(screen.getByText("Bienvenido!")).toBeInTheDocument();
    expect(
      screen.getByText("Ingrese su nombre de jugador")
    ).toBeInTheDocument();
  });

  it("no debería mostrar el diálogo si ya hay un nombre de jugador en sessionStorage", () => {
    sessionStorage.setItem("jugador_nombre", "Player1");

    render(<SetNickname />);

    // Verificar que el diálogo no está presente
    expect(screen.queryByText("Bienvenido!")).not.toBeInTheDocument();
  });

  it("debería permitir ingresar un nombre y guardarlo en sessionStorage", () => {
    render(<SetNickname />);

    const input = screen.getByLabelText("nickname");
    const saveButton = screen.getByText("Guardar");

    // Simular la entrada del nombre
    fireEvent.change(input, { target: { value: "PlayerTest" } });
    expect(input.value).toBe("PlayerTest");

    // Simular el clic en el botón "Guardar"
    fireEvent.click(saveButton);

    // Verificar que el nombre se ha guardado en sessionStorage
    expect(sessionStorage.getItem("jugador_nombre")).toBe("PlayerTest");
    expect(createName).toHaveBeenCalledWith("PlayerTest");
  });

  it("debería deshabilitar el botón 'Guardar' si el input está vacío", () => {
    render(<SetNickname />);

    const saveButton = screen.getByText("Guardar");

    // Verificar que el botón está deshabilitado cuando el input está vacío
    expect(saveButton).toBeDisabled();

    // Simular la entrada de un nombre válido
    const input = screen.getByLabelText("nickname");
    fireEvent.change(input, { target: { value: "PlayerTest" } });

    // Verificar que el botón está habilitado después de ingresar un nombre
    expect(saveButton).not.toBeDisabled();
  });
});
