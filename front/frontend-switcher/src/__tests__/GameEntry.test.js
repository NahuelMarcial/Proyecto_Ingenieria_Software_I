import React from "react";
import {render, fireEvent, screen, waitFor} from "@testing-library/react";
import GameEntry from "../principal/components/GameEntry";
import joinGameService from "../principal/services/joinGameService";

// Mock del servicio joinGameService
jest.mock("../principal/services/joinGameService");

// Mock del hook useNavigate
jest.mock("react-router-dom", () => ({
  useNavigate: jest.fn(),
}));

describe("GameEntry", () => {
  const partida_id = "123";
  const gameName = "Prueba Juego";
  const playersCount = 2;
  const playersLimit = 4;
  const password = 1234;
  const mockNavigate = jest.fn(); // Definir el mock de navigate

  beforeEach(() => {
    // Resetear los mocks antes de cada test
    jest.clearAllMocks();

    // Mockear useNavigate para que devuelva nuestra función mock
    require("react-router-dom").useNavigate.mockReturnValue(mockNavigate);
  });

  test("renderiza correctamente con los datos de la partida", () => {
    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
      />
    );

    // Verificar que los textos del nombre del juego y el número de jugadores se renderizan correctamente
    expect(screen.getByText(gameName)).toBeInTheDocument();
    expect(
      screen.getByText(`${playersCount}/${playersLimit}`)
    ).toBeInTheDocument();
  });

  test("llama al servicio joinGameService y navega al lobby al hacer clic en 'Unirse'", async () => {
    // Mockear el servicio joinGameService para que retorne una promesa resuelta
    joinGameService.mockResolvedValue("Partida Unida");

    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
        isPrivate={false}
      />
    );

    // Obtener el botón de "Unirse" y hacer clic en él
    const joinButton = screen.getByRole("button", {name: /unirse/i});
    fireEvent.click(joinButton);

    // Verificar que el servicio joinGameService fue llamado con el "partida_id" correcto
    await waitFor(() => {
      expect(joinGameService).toHaveBeenCalledWith(partida_id, "");
    });

    // Verificar que la función navigate fue llamada con la ruta correcta
    await waitFor(() => {
      expect(mockNavigate).toHaveBeenCalledWith(`/lobby/${partida_id}`);
    });
  });

  test("Renderizado de partida publica", async () => {
    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
        isPrivate={false}
      />
    );
    expect(screen.getByTestId("personicon")).toBeInTheDocument();
    expect(screen.queryByTestId("lockicon")).toBeNull();
  });

  test("Renderizado de partida privada", async () => {
    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
        isPrivate={true}
      />
    );
    expect(screen.getByTestId("personicon")).toBeInTheDocument();
    expect(screen.getByTestId("lockicon")).toBeInTheDocument();
  });

  test("Aparece el prop de ingresar partida cuando es privada", () => {
    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
        isPrivate={true}
      />
    );
    fireEvent.click(screen.getByRole("button", {name: /Unirse/i}))
    expect(screen.getByTestId("Dialogpassword")).toBeInTheDocument()
  });

  test("Ingreso contraseña incorrecta", async () => {
    joinGameService.mockRejectedValueOnce(new Error('Contraseña incorrecta'));
    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
        isPrivate={true}
      />
    );
    fireEvent.click(screen.getByRole("button", {name: /Unirse/i}));
    fireEvent.change(screen.getByTestId('input-pass'), {target: {value: '1234'}});
    fireEvent.click(screen.getByTestId("send-pass"));
    await waitFor(() => {
      expect(screen.getByText("La contraseña es incorrecta")).toBeInTheDocument();
    });
  });


  test("Ingreso contraseña correcta", async () => {
    joinGameService.mockResolvedValue('Partida unida');
    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
        isPrivate={true}
      />
    );
    fireEvent.click(screen.getByRole("button", {name: /Unirse/i}));
    fireEvent.change(screen.getByTestId('input-pass'), {target: {value: '1234'}});
    fireEvent.click(screen.getByTestId("send-pass"));
    await waitFor(() => {
      expect(joinGameService).toHaveBeenCalledWith(partida_id, '1234')
    });
  });
  test("Ingreso contraseña correcta no muestra mensaje de error", async () => {
    joinGameService.mockResolvedValueOnce({
        succes: true
      }
    )
    ;
    render(
      <GameEntry
        gameName={gameName}
        playersCount={playersCount}
        playersLimit={playersLimit}
        partida_id={partida_id}
        isPrivate={true}
      />
    );
    fireEvent.click(screen.getByRole("button", {name: /Unirse/i}));
    fireEvent.change(screen.getByTestId('input-pass'), {target: {value: '1234'}});
    fireEvent.click(screen.getByTestId("send-pass"));
    await waitFor(() => {
      expect(joinGameService).toHaveBeenCalledWith(partida_id, '1234')
      expect(screen.queryByText("La contraseña es incorrecta")).not.toBeInTheDocument();
    });

  });

});
