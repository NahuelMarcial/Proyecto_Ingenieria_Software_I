import React from "react";
import { Box, Typography } from "@mui/material"; // Importar componentes de MUI

const ForbiddenColor = ({ Color }) => {
  return (
    <Box // Caja que actúa como el contenedor principal
      sx={{
        display: "flex",
        alignItems: "center",
        padding: "10px",
        border: "5px solid",
        borderColor: Color, // El borde es de color del color prohibido
        borderRadius: "8px",
        backgroundColor: "grey.100", // Fondo gris claro
        width: "100%", 
      }}
    >
      <Typography variant="body1" sx={{ marginRight: "8px" }}>
        Color prohibido:
      </Typography>
      <Typography
        variant="h6"
        sx={{
          color: Color, // El color del texto será del color prohibido
          fontWeight: "bold",
        }}
      >
        {Color}
      </Typography>
    </Box>
  );
};

export default ForbiddenColor;
