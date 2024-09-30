import React from "react";
import { Card, CardContent, Typography, Button, Box } from "@mui/material";
import joinGameService from "../services/joinGameService";
import { useNavigate } from "react-router-dom";

const GameEntry = ({ gameName, playersCount, playersLimit, partida_id }) => {
  const navigate = useNavigate(); // hook para navegar entre rutas

  const handleJoinClick = async () => {
    try {
      // llamar al servicio para unirse a la partida
      const result = await joinGameService(partida_id);
      sessionStorage.setItem("partida_id", partida_id);
      sessionStorage.setItem("partida_nombre", gameName);
      console.log("Te has unido a la partida:", result);

      // redirigir a la página del lobby de la partida
      navigate(`/lobby/${partida_id}`);
    } catch (error) {
      console.error("Error al unirse a la partida:", error);
    }
  };

  return (
    <Card
      variant="outlined"
      sx={{
        position: "relative",
        marginBottom: 0, // Ajuste de espaciado según el theme
        backgroundColor: "primary.main", // Usar color primario desde el tema
        height: "44px",
        transition: "transform 0.3s, box-shadow 0.3s",
        boxShadow: 1, // Usar el primer nivel de sombras del tema
        "&:hover": {
          transform: "translateY(-5px)",
          boxShadow: 2, // Usar el segundo nivel de sombras del tema
        },
      }}
    >
      <CardContent sx={{ padding: 0 }}>
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Typography variant="h3" component="div">
            {gameName}
          </Typography>
          <Typography
            variant="h4"
            sx={{ position: "absolute", right: "120px" }}
          >
            {playersCount}/{playersLimit}
          </Typography>
          <Button
            variant="contained"
            color="secondary" // Usar color secundario desde el tema
            onClick={handleJoinClick}
            sx={{ fontWeight: "bold" }}
          >
            Unirse
          </Button>
        </Box>
      </CardContent>
    </Card>
  );
};

export default GameEntry;
