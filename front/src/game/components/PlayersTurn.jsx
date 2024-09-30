import React from "react";
import { Box, Typography } from "@mui/material"; // Importar componentes de MUI

const PlayersTurn = ({ PlayerName }) => {
  return (
    <Box // Caja que actúa como el contenedor principal
      sx={{
        display: "flex",
        alignItems: "center",
        padding: "10px",
        border: "5px solid",
        borderColor: "primary.main", // El borde es de color primario
        borderRadius: "8px",
        backgroundColor: "grey.100", // Fondo gris claro
        width: "100%",
      }}
    >
      <Typography variant="body1" sx={{ marginRight: "8px" }}>
        Turno de:
      </Typography>
      <Typography
        variant="h4"
        sx={{
          color: "primary.main", // El color del texto será del color principal
          fontWeight: "bold",
        }}
      >
        {PlayerName}
      </Typography>
    </Box>
  );
};

export default PlayersTurn;
