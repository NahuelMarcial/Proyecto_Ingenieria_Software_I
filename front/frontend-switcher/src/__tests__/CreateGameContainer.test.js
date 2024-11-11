import React from "react";
import { render, fireEvent, screen, waitFor } from "@testing-library/react";
import CreateGameContainer from "../principal/containers/CreateGameContainer";
import { handleCreateGame } from "../principal/services/createGameLogic";
import { MemoryRouter, BrowserRouter } from "react-router-dom";

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

  test("abre el formulario de creación de partida al hacer clic en el botón de creación", () => {
    render(
      <BrowserRouter>
        <CreateGameContainer />
      </BrowserRouter>
    );

    // Verificamos que el formulario no se muestra inicialmente
    expect(screen.queryByTestId("create-game-form")).not.toBeInTheDocument();

    // Simulamos el clic en el botón de crear partida
    fireEvent.click(screen.getByRole("button", { name: /CREAR PARTIDA/i }));

    // Verificamos que el formulario ahora está visible
    expect(screen.getByTestId("create-game-form")).toBeInTheDocument();
  });

  test("cierra el formulario al hacer clic en el botón 'Cancelar'", () => {
    render(
      <BrowserRouter>
        <CreateGameContainer />
      </BrowserRouter>
    );

    fireEvent.click(screen.getByRole("button", { name: /CREAR PARTIDA/i }));
    expect(screen.getByText("Crear Partida:")).toBeInTheDocument();
    expect(screen.queryByText("Crear")).toBeInTheDocument();

    fireEvent.click(screen.getByRole("button", { name: /Cancelar/i }));
  });

  test("deberia enviar el formulario correctamente y navega al lobby", async () => {
    handleCreateGame.mockResolvedValueOnce();

    render(
      <MemoryRouter>
        <CreateGameContainer />
      </MemoryRouter>
    );

    fireEvent.click(screen.getByText("CREAR PARTIDA"));

    // Completar el campo de nombre de partida utilizando el componente `GameNameInput`
    fireEvent.change(screen.getByPlaceholderText("Intoducir nombre..."), {
      target: { value: "Partida de Prueba", name: "nombre" },
    });

    // Seleccionar la cantidad de jugadores presionando el botón correspondiente
    fireEvent.click(screen.getByText("4")); // Hace clic en el botón con el valor 4

    fireEvent.click(screen.getByText("Crear"));

    // Esperar a que el formulario se envíe y navegue
    await waitFor(() => {
      expect(handleCreateGame).toHaveBeenCalledWith(
        {
          nombre: "Partida de Prueba",
          owner: "",
          max_jugadores: 4,
          password: "",
        },
        expect.any(Function), // setLoading
        expect.any(Function) // handleClose
      );
    });
  });
});
