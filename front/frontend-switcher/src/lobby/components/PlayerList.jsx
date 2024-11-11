import React from "react";
import { Box } from "@mui/material";
import PlayerCard from "./PlayerCard";

const PlayerList = ({ players, playersNames, maxPlayers }) => {
  const playerEntries = [
    { player: players.jugador1, name: playersNames.jugador1 },
    { player: players.jugador2, name: playersNames.jugador2 },
    { player: players.jugador3, name: playersNames.jugador3 },
    { player: players.jugador4, name: playersNames.jugador4 },
  ];

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 2,
        minHeight: "40vh",
      }}
    >
      {/* Para 2 jugadores en una fila */}
      {maxPlayers === 2 && (
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            gap: 2, // Ajusta el espacio entre los jugadores
            height: "100%", // Asegura que los jugadores estén centrados verticalmente
            width: "100%",
          }}
        >
          {playerEntries.slice(0, 2).map((entry, index) => (
            <PlayerCard
              key={index}
              player={entry.player}
              name={entry.name}
              face={index}
            />
          ))}
        </Box>
      )}

      {/* Para 3 jugadores: dos en la parte superior y uno centrado debajo */}
      {maxPlayers === 3 && (
        <>
          <Box
            sx={{
              display: "grid",
              gridTemplateColumns: "repeat(2, 1fr)",
              gap: { xs: 1, sm: 3 },
              width: "100%",
              justifyItems: "center",
            }}
          >
            {playerEntries.slice(0, 2).map((entry, index) => (
              <PlayerCard
                key={index}
                player={entry.player}
                name={entry.name}
                face={index}
              />
            ))}
          </Box>
          <Box display="flex" justifyContent="center" width="50%">
            <PlayerCard
              player={playerEntries[2].player}
              name={playerEntries[2].name}
              face={2}
            />
          </Box>
        </>
      )}

      {/* Para 4 jugadores: cuadrícula 2x2 */}
      {maxPlayers === 4 && (
        <Box
          sx={{
            display: "grid",
            gridTemplateColumns: "repeat(2, 1fr)",
            gridTemplateRows: "repeat(2, 1fr)",
            gap: { xs: 1, sm: 3 },
            width: "100%",
            justifyItems: "center",
          }}
        >
          {playerEntries.slice(0, 4).map((entry, index) => (
            <PlayerCard
              key={index}
              player={entry.player}
              name={entry.name}
              face={index}
            />
          ))}
        </Box>
      )}
    </Box>
  );
};

export default PlayerList;
