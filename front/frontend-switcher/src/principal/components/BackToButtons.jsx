import React from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@mui/material";
import { setupSocketConnection } from "../services/socketConnectionService";
import ExitToAppIcon from "@mui/icons-material/Login";

const BackToHome = () => {
  const navigate = useNavigate();

  const handleBackToHome = () => {
    sessionStorage.removeItem("partida_id");
    sessionStorage.removeItem("partida_nombre");
    sessionStorage.removeItem("turnStartTime");
    setupSocketConnection();
    navigate("/");
    window.location.reload();
  };

  return (
    <Button
      test-id="back-to-home"
      variant="contained"
      onClick={handleBackToHome}
      style={{ float: "right" }}
      sx={{
        width: "100%",
        height: "100%",
        backgroundColor: "secondary.main",
        color: "white",
        border: 1,
        borderColor: "secondary.dark",
        fontSize: "clamp(0.6rem, 1.5vw, 1.5rem)",
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: "secondary.light",
        },
      }}
    >
      Volver al Inicio
    </Button>
  );
};

const BackToLobby = ({ partidaId, partidaNombre }) => {
  const navigate = useNavigate();

  const handleBackToLobby = () => {
    if (partidaId) {
      sessionStorage.setItem("partida_id", partidaId);
      sessionStorage.setItem("partida_nombre", partidaNombre);
      setupSocketConnection();
    }
    navigate(`/lobby/${partidaId}`);
    window.location.reload();
  };

  return (
    <Button
      test-id="back-to-lobby"
      variant="contained"
      onClick={handleBackToLobby}
      sx={{
        width: { xs: "5%", sm: "5%", md: "10%" },
        maxHeight: "clamp(2.8rem, 3.5vw, 3.5rem)",
        backgroundColor: "primary.main",
        color: "white",
        border: 1,
        borderColor: "primary.dark",
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: "primary.light",
        },
      }}
    >
      <ExitToAppIcon sx={{ color: "black", fontSize: "40px" }} />
    </Button>
  );
};

const BackToGame = ({ partidaId, partidaNombre }) => {
  const navigate = useNavigate();

  const handleBackToGame = () => {
    if (partidaId) {
      sessionStorage.setItem("partida_id", partidaId);
      sessionStorage.setItem("partida_nombre", partidaNombre);
      setupSocketConnection();
    }
    navigate(`/game/${partidaId}`);
    window.location.reload();
  };

  return (
    <Button
      test-id="back-to-game"
      variant="contained"
      onClick={handleBackToGame}
      sx={{
        width: { xs: "5%", sm: "5%", md: "10%" },
        maxHeight: "clamp(2.8rem, 3.5vw, 3.5rem)",
        backgroundColor: "primary.main",
        color: "white",
        border: 1,
        borderColor: "primary.dark",
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: "primary.light",
        },
      }}
    >
      <ExitToAppIcon sx={{ color: "black", fontSize: "40px" }} />
    </Button>
  );
};

export { BackToHome, BackToLobby, BackToGame };
