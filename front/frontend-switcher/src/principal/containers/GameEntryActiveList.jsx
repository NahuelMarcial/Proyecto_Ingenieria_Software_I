import React, { useEffect, useState } from "react";
import gameEntryActiveService from "../services/gameEntryActiveService";
import GameEntryActive from "../components/GameEntryActive";
import { Box, List, ListItem, ListItemText, Typography } from "@mui/material";
import NotAvailableGames from "../components/NotAvailableGames";
import { socket } from "../../principal/services/socketConnectionService";

const GameEntryActiveList = () => {
  const player_id = sessionStorage.getItem("jugador_id");
  const partida_id = sessionStorage.getItem("partida_id");
  const [availableActiveGame, setAvailableActiveGame] = useState([]);

  const getActiveGames = async () => {
    try {
      const data = await gameEntryActiveService(player_id);
      const filteredGames = data.filter(
        (game) => game.id !== Number(partida_id)
      );

      const gameWithState = filteredGames.map((games) => {
        let isYourTurn = false;
        let gameState = 1;

        if (games.ganador) {
          gameState = 0;
        } else if (games.iniciada && games.owner !== "") {
          gameState = 2;
        } else if (games.iniciada && games.owner === "") {
          gameState = 0;
        } else {
          gameState = 1;
        }

        if (games.tu_turno && games.iniciada) {
          isYourTurn = true;
        }
        return { ...games, gameState, isYourTurn };
      });
      setAvailableActiveGame(gameWithState);
    } catch (e) {
      throw e;
    }
  };

  useEffect(() => {
    getActiveGames();
  }, []);

  useEffect(() => {
    socket.on("partida_iniciada", () => {
      getActiveGames();
    });
    socket.on("actualizar_partidas_activas", (data) => {
      console.log(
        "se actualizan las partidas activas",
        data.player_id.id_player,
        player_id
      );
      if (data.player_id.id_player === player_id) {
        getActiveGames();
      }
      if (data.player_id === player_id) {
        getActiveGames();
      }
    });
    return () => {
      socket.off("partida_iniciada");
      socket.off("actualizar_partidas_activas");
    };
  }, [socket]);

  return (
    <Box
      sx={{
        padding: { xs: 1, sm: 2 },
        borderRadius: 2,
        border: "1px solid #ddd",
        bgcolor: "#f8f9fa",
        maxWidth: "80%",
        minWidth: "90%",
        margin: "0 auto",
        height: "94.5%",
      }}
    >
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
          Mis Partidas:
        </Typography>
      </Box>
      <Box
        sx={{
          height: { xs: "55vh", sm: "60vh" },
          overflowY: "auto",
          padding: 1,
        }}
      >
        {availableActiveGame.length > 0 ? (
          <List>
            {availableActiveGame.map((data) => (
              <ListItem key={data.id} sx={{ padding: 0, marginBottom: "5px" }}>
                <ListItemText>
                  <GameEntryActive
                    gameId={data.id}
                    gameName={data.nombre}
                    gameState={data.gameState}
                    isMyTurn={data.isYourTurn}
                    isIniciada={data.iniciada}
                  />
                </ListItemText>
              </ListItem>
            ))}
          </List>
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

export default GameEntryActiveList;
