// Conetenerdor para la lista de partidas disponibles
import React, { useState, useEffect } from "react";
import GameEntry from "../components/GameEntry";
import { getGameListServices } from "../services/getGameListServices";
import { Box, Typography, List, ListItem, ListItemText } from "@mui/material";

const GameListContainer = ({ socket }) => {
  const [availableGames, setAvailableGames] = useState([]); // estado para las partidas disponibles

  // obtener las partidas
  const fetchGames = async () => {
    try {
      const games = await getGameListServices();
      setAvailableGames(games);
    } catch (error) {
      console.error("Error al obtener las partidas:", error);
    }
  };

  useEffect(() => {
    // fetch games al montar el componente
    fetchGames();

    // escuchar evento partida_creada para actualizar la lista de partidas
    socket.on("partida_creada", () => {
      console.log("Evento 'partida_creada' recibido");
      fetchGames();
    });

    // escuchar evento jugador_unido para actualizar la lista de partidas
    socket.on("jugador_unido", () => {
      console.log("Evento 'jugador_unido' recibido");
      fetchGames();
    });

    socket.on("jugador_abandona", (data) => {
      console.log("El jugador", data, " abandono la partida");
      fetchGames();
    });

    // limpiar eventos al desmontar
    return () => {
      socket.off("partida_creada");
      socket.off("jugador_unido");
      socket.off("jugador_abandona");
    };
  }, []);

  return (
    <Box
      sx={{
        padding: 2,
        borderRadius: 2,
        border: "1px solid #ddd",
        bgcolor: "#f8f9fa",
        maxWidth: "1000px",
        margin: "0 auto",
      }}
    >
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          borderBottom: "1px solid #ddd",
          paddingBottom: 1,
        }}
      >
        <Typography variant="h2" color="secondary">
          Partidas disponibles...
        </Typography>
      </Box>
      <Box sx={{ height: "450px", overflowY: "auto", padding: 1 }}>
        {availableGames.length > 0 ? (
          <List>
            {availableGames.map((game) => (
              <ListItem key={game.id} sx={{ padding: 0, marginBottom: "1px" }}>
                <ListItemText>
                  <GameEntry
                    gameName={game.nombre}
                    playersCount={game.cantidad_jugadores}
                    playersLimit={game.max_jugadores}
                    partida_id={game.id}
                  />
                </ListItemText>
              </ListItem>
            ))}
          </List>
        ) : (
          <Typography variant="h4" sx={{ marginTop: 2 }}>
            No hay mesas disponibles todavía! :(
          </Typography>
        )}
      </Box>
    </Box>
  );
};

export default GameListContainer;
