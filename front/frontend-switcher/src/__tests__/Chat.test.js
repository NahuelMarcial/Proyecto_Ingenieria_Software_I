import React from "react";
import { render, screen, fireEvent, act } from "@testing-library/react";
import Chat from "../game/containers/Chat";
import { io } from "socket.io-client"; // Asegúrate de que el cliente de socket esté disponible
import getNameById from "../game/services/getNameById";
import userEvent from "@testing-library/user-event";

// Mock del servicio getNameById
jest.mock("../game/services/getNameById");

// Mock del socket
const socket = {
  on: jest.fn(),
  emit: jest.fn(),
  off: jest.fn(),
};

describe("Chat Component", () => {
  const jugadorId = "1";
  const partidaId = 123; // ID de partida para las pruebas

  beforeAll(() => {
    window.HTMLElement.prototype.scrollIntoView = jest.fn();
  });

  beforeEach(() => {
    sessionStorage.setItem("partida_id", partidaId); // Configura el ID de partida en el sessionStorage
    getNameById.mockResolvedValue("Jugador1"); // Mockea la respuesta del nombre del jugador
  });

  afterEach(() => {
    jest.clearAllMocks(); // Limpia los mocks después de cada prueba
  });

  test("should render correctly", () => {
    render(<Chat socket={socket} jugadorId={jugadorId} />);

    // Verifica que el campo de entrada y el botón estén en el documento
    expect(
      screen.getByPlaceholderText(/escribe un mensaje.../i)
    ).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /enviar/i })).toBeInTheDocument();
  });

  test("should send a message and display it", async () => {
    render(<Chat socket={socket} jugadorId={jugadorId} />);

    const input = screen.getByPlaceholderText("Escribe un mensaje...");
    const button = screen.getByRole("button", { name: /enviar/i });

    // Simula la escritura en el campo de entrada y el clic en el botón de envío
    await act(async () => {
      fireEvent.change(input, { target: { value: "Hola, mundo!" } });
      fireEvent.click(button);
    });

    // Verifica que el socket emitió el mensaje correctamente
    expect(socket.emit).toHaveBeenCalledWith("chat_message", {
      message: "Hola, mundo!",
      playerId: "Jugador1",
      time: expect.any(String),
      partida_id: "123",
      isLogSystem: false,
    });

    // Simula recibir el mensaje
    const newMessageData = {
      playerId: "Jugador1",
      message: "Hola, mundo!",
      time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      partida_id: sessionStorage.getItem("partida_id"),
      isLogSystem: false,
    };

    // Llama a la función con el mensaje simulado
    socket.on.mock.calls[0][1](newMessageData); 

    // Verifica que el mensaje se muestra en el chat
    expect(await screen.findByText("Jugador1 - " + newMessageData.time)).toBeInTheDocument();
    expect(screen.getByText("Hola, mundo!")).toBeInTheDocument();
  });

  test("should not display messages from another game", async () => {
    render(<Chat socket={socket} jugadorId={jugadorId} />);
    const anotherPartidaId = 456; // ID de otra partida

    // Simula un mensaje recibido de otra partida
    socket.on.mockImplementation((event, callback) => {
      if (event === "receive_chat_message") {
        callback({
          playerId: "Jugador3",
          message: "Este mensaje no debería aparecer",
          time: new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          }),
          partida_id: anotherPartidaId,
          isLogSystem: false,
        });
      }
    });

    // Asegúrate de que el mensaje no esté en el documento
    expect(
      await screen.queryByText("Este mensaje no debería aparecer")
    ).not.toBeInTheDocument();
  });

  test("should display system logs in the chat", async () => {
    render(<Chat socket={socket} jugadorId={jugadorId} />);

    // Simula la emisión de un evento de log del sistema
    await act(async () => {
      // Simulamos un evento de log
      socket.on.mock.calls[0][1]({
        playerId: "Jugador1",
        message: "Jugador1 se ha desconectado.",
        time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
        partida_id: sessionStorage.getItem("partida_id"),
        isLogSystem: true,
      });
    });

    // Verifica que el log se muestra en el chat como un mensaje
    expect(await screen.findByText("Jugador1 - " + new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }))).toBeInTheDocument();
    expect(screen.getByText("Jugador1 se ha desconectado.")).toBeInTheDocument();
  });
});
