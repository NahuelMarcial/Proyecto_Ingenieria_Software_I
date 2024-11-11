import React from "react";
import { Box, Card, CardContent, Typography } from "@mui/material";
import { BackToLobby, BackToGame } from "./BackToButtons";
import GameState from "./GameState";
import IsMyTurn from "./IsMyTurn";

const GameEntryActive = ({
  gameId,
  gameName,
  gameState,
  isMyTurn,
  isIniciada,
}) => {
  const truncateName = (name, maxLength) => {
    return name.length > maxLength ? name.slice(0, maxLength) + "..." : name;
  };

  return (
    <Card
      sx={{
        marginBottom: 0,
        backgroundColor: "secondary.light", // Usar color secundario desde el tema
        height: { xs: "30px", sm: "40px", md: "44px" }, // Ajuste de altura según el theme
        transition: "transform 0.3s, box-shadow 0.3s",
        boxShadow: 1, // Usar el primer nivel de sombras del tema
        "&:hover": {
          transform: "translateY(-5px)",
          boxShadow: 2, // Usar el segundo nivel de sombras del tema
        },
      }}
    >
      <CardContent
        sx={{
          padding: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
          marginBottom={1}
          sx={{ width: "100%", height: "100%" }}
        >
          <Box
            display="flex"
            gap={1}
            marginBottom={1}
            sx={{ maxWidth: "50%", maxHeight: "100%" }}
          >
            <Typography variant="h3" component="div">
              {truncateName(gameName, 15)}
            </Typography>
          </Box>
          <Box
            display="flex"
            alignItems="center"
            justifyContent="flex-end"
            width="50%"
            sx={{ gap: 0.6 }}
          >
            {isMyTurn && gameState !== 0 && <IsMyTurn />}
            <GameState gameState={gameState} />
            {isIniciada ? (
              <BackToGame partidaId={gameId} partidaNombre={gameName} />
            ) : (
              <BackToLobby partidaId={gameId} partidaNombre={gameName} />
            )}
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
};

export default GameEntryActive;
