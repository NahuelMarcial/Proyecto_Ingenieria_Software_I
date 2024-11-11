import React from "react";
import { CardContent, Typography, Box, Paper } from "@mui/material";
import getFaceIcon from "./Faces";
import StarIcon from "@mui/icons-material/Star";
import CrownIcon from "../../assets/icons/CrownIcon";

const PlayerCard = ({ player, name, face }) => {
  const isOccupied = !!player; // Verificar si hay un jugador ocupando la tarjeta

  return (
    <Paper
      elevation={isOccupied ? 2 : 0}
      sx={{
        width: "100%",
        height: "100%",
        minHeight: "clamp(100px, 20vw, 200px)",
        backgroundColor: isOccupied ? "primary.main" : "grey.300",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <CardContent>
        <Box
          position="relative"
          display="flex"
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
        >
          {/* Mostrar la corona si el jugador es el líder */}
          {face === 0 && isOccupied && (
            <CrownIcon 
              sx={{ 
                fontSize: "clamp(26px, 4vw, 42px)", 
                position: "absolute", 
                top: "-30%",
              }} 
            />
          )}
          {/* Mostrar el ícono según `face` */}
          {getFaceIcon(face, isOccupied)}
          {/* Nombre del jugador o placeholder */}
          <Paper
            sx={{
              display: "flex",
              justifyContent: "center",
              padding: "clamp(0.5rem, 1vw, 1rem)",
              width: "100%",
              backgroundColor: isOccupied ? "primary.dark" : "grey.300",
            }}
          >
            <Typography
              variant="h3"
              fontSize={"clamp(0.675rem, 2vw, 1.2rem)"}
              color={isOccupied ? "white" : "text.secondary"}
              sx={{
                wordBreak: "break-word",
                textAlign: "center",
              }}
            >
              {isOccupied ? name : "Disponible"}
            </Typography>
          </Paper>
        </Box>
      </CardContent>
    </Paper>
  );
};

export default PlayerCard;
