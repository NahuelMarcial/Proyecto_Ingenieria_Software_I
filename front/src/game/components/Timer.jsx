import React from "react";
import { Box, Typography } from "@mui/material"; // Importar componentes de MUI

const Timer = ({ Time, TimeIsEnding }) => {
  return (
    <Box // Caja que actúa como el contenedor principal del temporizador
      sx={{
        display: "flex",
        alignItems: "center",
        padding: "10px",
        border: "5px solid",
        borderColor: TimeIsEnding ? "error.main" : "primary.main", // Cambia el borde según el estado
        borderRadius: "8px",
        backgroundColor: TimeIsEnding ? "error.light" : "grey.100", // Fondo cambia si el tiempo está por acabar
        width: "100%", 
      }}
    >
      <Typography variant="body1" sx={{ marginRight: "8px" }}>
        Timer:
      </Typography>
      <Typography
        variant="h6"
        sx={{
          color: TimeIsEnding ? "error.main" : "text.primary", // Cambia el color del texto
          fontWeight: "bold",
        }}
      >
        {Time}
      </Typography>
    </Box>
  );
};

export default Timer;
