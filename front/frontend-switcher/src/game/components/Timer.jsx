import React from "react";
import { Box, Typography } from "@mui/material";
import AccessTimeIcon from "@mui/icons-material/AccessTime"; // Importa el ícono de reloj

const Timer = ({ Time, TimeIsEnding }) => {
  // Calcula el porcentaje de tiempo restante (de 120 a 0 segundos)
  const timePercentage = (Time / 120) * 100;

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "flex-end",
        padding: "0", // Espaciado para hacer la franja más alta
        height: "390px", // Altura fija para la franja
        width: "40px",
        border: "3px solid",
        borderColor: TimeIsEnding ? "error.main" : "black",
        borderRadius: "5px",
        backgroundColor: "grey.100",
        position: "relative", // Para permitir posicionamiento absoluto del contenido
      }}
    >
      {/* Franja de tiempo restante */}
      <Box
        sx={{
          width: "100%",
          height: `${(timePercentage * 390) / 100}px`, // Proporción de tiempo restante (312px es la altura disponible después del padding)
          backgroundColor: TimeIsEnding ? "error.main" : "primary.main",
          transition: "height 0.5s linear",
        }}
      />

      {/* Ícono de reloj en el centro */}
      <AccessTimeIcon
        sx={{
          position: "absolute",
          top: "50%", // Centra verticalmente
          left: "50%", // Centra horizontalmente
          transform: "translate(-50%, -50%)", // Ajusta el desplazamiento para centrar
          fontSize: "30px", // Tamaño del ícono
          color: TimeIsEnding ? "error.main" : "black", // Cambia el color según el tiempo restante
        }}
      />

      {/* Texto del temporizador */}
      <Typography
        variant="h4"
        sx={{
          position: "absolute",
          bottom: "150px", // Coloca el texto cerca de la parte inferior
          color: TimeIsEnding ? "error.main" : "text.primary",
          fontWeight: "bold",
        }}
      >
        {Time}
      </Typography>
    </Box>
  );
};

export default Timer;
