import React from "react";
import SportsScoreIcon from "@mui/icons-material/SportsScore";
import LoopIcon from "@mui/icons-material/Loop";
import HourglassEmptyIcon from "@mui/icons-material/HourglassEmpty";
import { Box } from "@mui/material";
import "./GameState.css";

const GameState = ({ gameState }) => {
  const getStatusIcon = (status) => {
    switch (status) {
      case 0: // Finalizada
        return <SportsScoreIcon sx={{ fontSize: "30px" }} />;
      case 2: // En curso
        return <LoopIcon className="rotating-icon" sx={{ fontSize: "30px" }} />;
      case 1: // En espera
        return <HourglassEmptyIcon sx={{ fontSize: "30px" }} />;
      default:
        return null;
    }
  };

  const getBorderColor = (status) => {
    switch (status) {
      case 0:
        return "error.main"; // Finalizada
      case 2:
        return "success.main"; // En curso
      case 1:
        return "grey.800"; // En espera
      default:
        return "transparent";
    }
  };

  return (
    <Box
      data-testid="game-state"
      sx={{
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        borderRadius: 2,
        bgcolor: "grey.100",
        border: 3,
        borderColor: getBorderColor(gameState),
        padding: 1,
        width: { xs: "5%", sm: "5%", md: "10%" },
        minWidth: "clamp(1.8rem, 2.0vw, 2.0rem)",
        maxHeight: "clamp(1.8rem, 2.0vw, 2.0rem)",
      }}
    >
      {getStatusIcon(gameState)}
    </Box>
  );
};

export default GameState;
