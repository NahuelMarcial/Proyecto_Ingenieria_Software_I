import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { io } from "socket.io-client";
import theme from "./theme";
import { ThemeProvider } from "@mui/material/styles";

import Principal from "./principal/containers/Principal";
import Lobby from "./lobby/containers/Lobby";
import Game from "./game/containers/Game";

// conexion al socket
const socket = io("https://proyecto-ingenieria-software-i.onrender.com/", {
  path: "/sockets/socket_connection",
  transports: ["websocket"],
  reconnectionAttempts: 5,
  reconnectionDelay: 2000,
});

// funcion para asignar un jugador_id a cada usuario que ingresa a la pagina
function getPlayerId() {
  let jugador_id = sessionStorage.getItem("jugador_id");
  if (!jugador_id) {
    jugador_id = "player-" + Math.random().toString(36).substring(2, 9);
    sessionStorage.setItem("jugador_id", jugador_id);
  }
  return jugador_id; // un identifiador único para el jugador
}

function App() {
  useEffect(() => {
    // Escuchar el evento 'connect'
    socket.on("connect", () => {
      const id = getPlayerId();

      sessionStorage.setItem("sid", socket.id);
      // logica para guardar socket anterior, cuando el usuario recarga la pagina
      let previd = sessionStorage.getItem("prevsid");
      sessionStorage.setItem("prevsid", socket.id);
      if (!previd) {
        previd = socket.id;
      }
      const partida_id = sessionStorage.getItem("partida_id");
      if (!partida_id) {
        socket.emit("connect_player", {
          sid: socket.id,
          previd: previd,
          partida_id: "/",
        });
      } else {
        socket.emit("connect_player", {
          sid: socket.id,
          previd: previd,
          partida_id: partida_id,
        });
      }
    });

    // Cleanup on unmount
    return () => {
      if (socket.readyState === 1) {
        socket.close(); // el socket se cierra solo si esta abierto, evita warnings
      }
    };
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <Router>
        <Routes>
          <Route path="/" element={<Principal socket={socket} />} />
          <Route
            path="/lobby/:partida_id"
            element={<Lobby socket={socket} />}
          />
          <Route path="/game/:partida_id" element={<Game socket={socket} />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
