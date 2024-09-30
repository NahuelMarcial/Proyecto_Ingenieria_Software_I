import React, { useState, useEffect } from "react";
import Grid from "@mui/material/Grid2";
import { useNavigate } from "react-router-dom";

import getGamePlayers from "../services/getGamePlayers";
import getFichas from "../services/getFichas";
import Disconectgamestarted from "../services/DisconectGameStarte";
import deleteGame from "../services/deleteGame";

import RenderTables from "./RenderTables";

const Game = ({ socket }) => {
  const navigate = useNavigate();
  const partida_id = sessionStorage.getItem("partida_id");
  const [players, setPlayers] = useState([]); // Modificador de jugadores
  const [fichas, setFichas] = useState([]); // Modificador de fichas

  // Funcion para desconectar al jugador de la partida
  const Disconect = () => {
    const player_id = sessionStorage.getItem("jugador_id");
    const sid = sessionStorage.getItem("sid");
    Disconectgamestarted(partida_id, player_id, sid, navigate);
  };

  // Funcion para desconectar al ultimo jugador de la partida
  const Disconect2 = () => {
    const partida_id = sessionStorage.getItem("partida_id");
    const sid = sessionStorage.getItem("sid");
    const response = deleteGame(partida_id, sid);
    if (response) {
      sessionStorage.removeItem("partida_id");
      sessionStorage.removeItem("partida_nombre");
      sessionStorage.removeItem("players");
      navigate("/");
    }
  };

  // Funcion para obtener los jugadores de la partida
  const fetchPlayers = async () => {
    const jugadores = await getGamePlayers(partida_id);
    sessionStorage.setItem("players", JSON.stringify(jugadores));
    //busca jugadores en la mesa por id
    setPlayers(jugadores);
  };

  // Funcion para obtener las fichas de la partida
  const fetchFichas = async () => {
    const fetchedFichas = await getFichas(partida_id);
    // busca las fichas en la partida por id
    setFichas(fetchedFichas);
  };

  useEffect(() => {
    fetchPlayers(); // Obtiene los jugadores de la partida
    fetchFichas(); // Obtiene las fichas de la partida

    socket.on("jugador_abandona_ini", () => {
      console.log("Jugador abandona la partida");
      fetchPlayers();
    });
  }, [partida_id]);

  return (
    <div className="game-container">
      <Grid
        container
        direction={"column"}
        spacing={2}
        justifyContent="center"
        alignItems="center"
      >
        <RenderTables
          players={players}
          fichas={fichas}
          Disconect={Disconect}
          Disconect2={Disconect2}
          socket={socket}
        />
      </Grid>
    </div>
  );
};

export default Game;
