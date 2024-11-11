import React from "react";
import { Box } from "@mui/material";
import PersonOffIcon from "@mui/icons-material/PersonOff"; // Importar ícono

const PlayerDisconnect = ({ width, height }) => {
  return (
    <Box
      sx={{
        width,
        height,
        padding: 0,
        borderRadius: 2,
        border: "3px solid #ddd",
        bgcolor: "#f8f9fa",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        color: "gray",
      }}
    >
      <PersonOffIcon fontSize="large" /> {/* Ícono de persona desconectada */}
    </Box>
  );
};

export default PlayerDisconnect;
