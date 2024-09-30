import React from "react";
import { Card, CardContent, Typography, Box } from "@mui/material";
import PersonIcon from "@mui/icons-material/Person"; // Importar el icono de Material UI

const PlayerCard = ({ player }) => {
  const isOccupied = !!player; // Verificar si hay un jugador ocupando la tarjeta

  return (
    <Card
      sx={{
        width: "200px",
        height: "200px",
        backgroundColor: isOccupied ? "primary.main" : "grey.300",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <CardContent>
        <Box
          display="flex"
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
        >
          {/* Mostrar el ícono */}
          <PersonIcon
            sx={{
              fontSize: "40px",
              color: isOccupied ? "white" : "text.secondary",
              mb: 1,
            }}
          />
          {/* Nombre del jugador o placeholder */}
          <Typography
            variant="h4"
            color={isOccupied ? "white" : "textSecondary"}
          >
            {isOccupied ? player : "Disponible"}
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );
};

export default PlayerCard;
