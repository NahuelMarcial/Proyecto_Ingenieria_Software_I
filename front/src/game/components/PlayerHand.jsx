import React from "react";
import FigureCard from "./FigureCard";
import MovCard from "./MovCard";
import { Box, Grid2, Typography } from "@mui/material";

const PlayerHand = ({
  jugador_id,
  isHost,
  figureCards = [],
  movCards = [],
}) => {
  return (
    <Box
      sx={{
        display: "inline-block", // el ancho se ajusta automaticamente al contenido
        padding: 2,
        borderRadius: 2,
        border: "1px solid #ddd",
        bgcolor: "#f8f9fa",
      }}
    >
      <Typography variant="h3">Mano del Jugador {jugador_id}</Typography>
      <Grid2 container spacing={2}>
        {/* Mostrar siempre las cartas de figura */}
        {figureCards.map((figure, index) => (
          <Grid2 item="true" key={index}>
            <FigureCard imageSrc={figure.imageSrc} title={figure.title} />
          </Grid2>
        ))}

        {/* Mostrar cartas de movimiento solo si es host */}
        {isHost &&
          movCards.map((mov, index) => (
            <Grid2 item="true" key={index}>
              <MovCard imageSrc={mov.imageSrc} title={mov.title} />
            </Grid2>
          ))}
      </Grid2>
    </Box>
  );
};

export default PlayerHand;
