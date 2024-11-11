import React, { useState, useEffect } from "react";
import GameEntry from "../components/GameEntry";
import { getGameListServices } from "../services/getGameListServices";
import { Box, Typography, List, ListItem, ListItemText } from "@mui/material";
import SearchGames from "../components/SearchGames";
import NotAvailableGames from "../components/NotAvailableGames";
import NotFoundGames from "../components/NotFoundGames";

const GameListContainer = ({ socket }) => {
  const [availableGames, setAvailableGames] = useState([]); // estado para las partidas disponibles
  const [filteredGames, setFilteredGames] = useState([]); // estado para las partidas filtradas
  const player_id = sessionStorage.getItem("jugador_id");

  // obtener las partidas
  const fetchGames = async () => {
    try {
      const games = await getGameListServices(player_id);
      setAvailableGames(games);
      setFilteredGames(games);
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

    socket.on("jugador_unido", () => {
      console.log("Evento 'jugador_unido' recibido");
      fetchGames();
    });

    socket.on("jugador_abandona", (data) => {
      console.log("El jugador", data, " abandonó la partida");
      fetchGames();
    });

    socket.on("partida_borrada", () => {
      console.log("Evento 'partida_borrada' recibido");
      fetchGames();
    });

    // limpiar eventos al desmontar
    return () => {
      socket.off("partida_creada");
      socket.off("jugador_unido");
      socket.off("jugador_abandona");
      socket.off("partida_borrada");
    };
  }, []);

  return (
    <Box
      sx={{
        padding: { xs: 1, sm: 2 },
        borderRadius: 2,
        border: "1px solid #ddd",
        bgcolor: "#f8f9fa",
        maxWidth: "95%",
        minWidth: "95%",
        margin: "0 auto",
      }}
    >
      {/* Encabezado */}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          borderBottom: "1px solid #ddd",
          paddingBottom: 2,
        }}
      >
        <Typography
          variant="h2"
          color="secondary"
          sx={{
            marginTop: 0.5,
            marginLeft: { xs: 1, sm: 1.5 },
          }}
        >
          Partidas disponibles...
        </Typography>
        <SearchGames
          availableGames={availableGames}
          onFilter={setFilteredGames}
        />
      </Box>

      {/* Lista de partidas */}

      <Box
        sx={{
          height: { xs: "55vh", sm: "60vh" },
          overflowY: "auto",
          padding: 1,
        }}
      >
        {availableGames.length > 0 ? (
          filteredGames.length > 0 ? (
            <List>
              {filteredGames.map((game) => (
                <ListItem
                  key={game.id}
                  sx={{ padding: 0, marginBottom: "5px" }}
                >
                  <ListItemText>
                    <GameEntry
                      gameName={game.nombre}
                      playersCount={game.cantidad_jugadores}
                      playersLimit={game.max_jugadores}
                      partida_id={game.id}
                      isPrivate={game.password}
                      isDifficult={game.dificil}
                    />
                  </ListItemText>
                </ListItem>
              ))}
            </List>
          ) : (
            <List>
              <ListItem sx={{ padding: 0 }}>
                <NotFoundGames />
              </ListItem>
            </List>
          )
        ) : (
          <List>
            <ListItem sx={{ padding: 0 }}>
              <NotAvailableGames />
            </ListItem>
          </List>
        )}
      </Box>
    </Box>
  );
};

export default GameListContainer;
