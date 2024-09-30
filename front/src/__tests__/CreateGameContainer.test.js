import React from "react";
import { render, fireEvent, screen, waitFor } from "@testing-library/react";
import CreateGameContainer from "../principal/containers/CreateGameContainer";
import { handleCreateGame } from "../principal/services/createGameLogic";
import { MemoryRouter } from "react-router-dom";

// Mock del servicio
jest.mock("../principal/services/createGameLogic");
const mockNavigate = jest.fn();
jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useNavigate: () => mockNavigate,
}));

describe("CreateGameContainer", () => {
  beforeEach(() => {
    jest.clearAllMocks();
    // Mockear el sessionStorage para el nombre del dueño
    window.sessionStorage.setItem("owner", "Ivanito");
    window.sessionStorage.setItem("partida_id", "123");
  });

  test("envía el formulario correctamente y navega al lobby", async () => {
    handleCreateGame.mockResolvedValueOnce();

    render(
      <MemoryRouter>
        <CreateGameContainer />
      </MemoryRouter>
    );

    fireEvent.click(screen.getByText("CREAR PARTIDA"));

    // Completar el formulario, el campo 'owner' lo toma de sessionStorage
    fireEvent.change(screen.getByLabelText("Nombre de la Partida *"), {
      target: { value: "Partida de Prueba", name: "nombre" },
    });
    fireEvent.change(screen.getByLabelText("Máximo de Jugadores *"), {
      target: { value: 4, name: "max_jugadores" },
    });

    fireEvent.click(screen.getByText("Crear"));

    // Esperar a que el formulario se envíe y navegue
    await waitFor(() => {
      expect(handleCreateGame).toHaveBeenCalledWith(
        {
          nombre: "Partida de Prueba",
          owner: "", // El valor del dueño viene del sessionStorage
          max_jugadores: "4",
        },
        expect.any(Function), // setLoading
        expect.any(Function) // handleClose
      );
      expect(mockNavigate).toHaveBeenCalledWith("/lobby/123");
    });
  });
});
