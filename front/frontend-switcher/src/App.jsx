import React, { useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import { ThemeProvider } from "@mui/material/styles";
import theme from "./configs/theme";

import Principal from "./principal/containers/Principal";
import Lobby from "./lobby/containers/Lobby";
import Game from "./game/containers/Game";

import {
  socket,
  setupSocketConnection,
  closeSocketConnection,
} from "./principal/services/socketConnectionService";

function App() {
  useEffect(() => {
    setupSocketConnection();

    return () => {
      closeSocketConnection();
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
