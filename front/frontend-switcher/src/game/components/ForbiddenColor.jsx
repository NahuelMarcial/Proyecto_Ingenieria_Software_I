import React from "react";
import { Box } from "@mui/material";
import BlockIcon from "@mui/icons-material/Block"; // Importar el icono de bloqueo

const ForbiddenColor = ({ color }) => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column", // Coloca el contenido en forma vertical
        alignItems: "center",
        justifyContent: "center", // Centra el contenido vertical y horizontalmente
        padding: "20px 0", // Espaciado para hacer la franja más alta
        height: "352px", // Altura fija para la franja
        width: "40px", // Ancho de la franja
        backgroundColor: color, // Fondo gris claro
        borderRadius: "5px", // Bordes redondeados
        border: "3px solid black",
      }}
    >
      <BlockIcon sx={{ fontSize: 35, color: "black" }} />{" "}
      {/* Ícono de bloqueo */}
    </Box>
  );
};

export default ForbiddenColor;
