// src/components/PlayerList.jsx
import React from "react";
import PlayerCard from "./PlayerCard";

const PlayerList = ({ players }) => {
  return (
    <div
      style={{
        display: "flex",
        gap: "16px", // espacio entre tarjetas
        justifyContent: "center", // centrar horizontalmente
        flexWrap: "wrap", // permitir que las tarjetas se muevan a la siguiente fila si no caben
      }}
    >
      <PlayerCard player={players.jugador1} />
      <PlayerCard player={players.jugador2} />
      <PlayerCard player={players.jugador3} />
      <PlayerCard player={players.jugador4} />
    </div>
  );
};

export default PlayerList;
