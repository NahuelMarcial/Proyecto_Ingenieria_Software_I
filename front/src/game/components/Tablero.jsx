import React, { useState } from "react";
import Ficha from "./Ficha"; // Asegúrate de importar el componente
import { Box } from "@mui/material";

const handleColor = (colorEsp) => {
  const colors = {
    rojo: "red",
    azul: "blue",
    amarillo: "yellow",
    verde: "green",
  };
  return colors[colorEsp] || colorEsp; // Devuelve el color en inglés o el original si no se encuentra
};

const Tablero = ({ fichas }) => {
  return (
    <Box
      sx={{
        width: "100%",
        height: "100%",
        backgroundColor: "white",
        display: "grid",
        gridTemplateColumns: "repeat(6, 1fr)", // 6 columnas
        gridTemplateRows: "repeat(6, 1fr)", // 6 filas
        gap: "5px", // Espaciado entre las celdas del tablero
        border: "solid black",
        borderRadius: "5px",
        boxShadow: "0 0 10px rgba(0, 0, 0, 0.2)",
      }}
    >
      {fichas &&
        fichas.map((ficha, index) => (
          <Ficha
            key={index}
            pos_x={ficha.pos_x}
            pos_y={ficha.pos_y}
            color={handleColor(ficha.color)}
          />
        ))}
    </Box>
  );
};

export default Tablero;
