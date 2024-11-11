import { io } from "socket.io-client";
import URL_API from "../../configs/urlAPI";

// Conexión del socket
const socket = io(URL_API, {
  path: "/sockets/socket_connection",
  transports: ["websocket"],
  reconnection: true,
  reconnectionAttempts: 10000,
  reconnectionDelay: 500,
});

function getPlayerId() {
  let jugador_id = sessionStorage.getItem("jugador_id");
  if (!jugador_id) {
    jugador_id = "player-" + Math.random().toString(36).substring(2, 9);
    sessionStorage.setItem("jugador_id", jugador_id);
  }
  return jugador_id;
}

// Función para gestionar la reconexión del socket
function setupSocketConnection() {
  socket.on("connect", () => {
    const player_id = getPlayerId();
    sessionStorage.setItem("sid", socket.id);

    let previd = sessionStorage.getItem("prevsid");
    sessionStorage.setItem("prevsid", socket.id);
    if (!previd) {
      previd = socket.id;
    }
    const partida_id = sessionStorage.getItem("partida_id") || "/";

    socket.emit("connect_player", {
      sid: socket.id,
      previd,
      partida_id,
      player_id,
    });
  });
}

// Función para cerrar el socket cuando se desmonta el componente
function closeSocketConnection() {
  if (socket.readyState === 1) {
    socket.close();
  }
}

export { socket, setupSocketConnection, closeSocketConnection };
