import React, { useState, useEffect } from "react";
import Grid from "@mui/material/Grid2";
import { useNavigate } from "react-router-dom";
import { Typography } from "@mui/material";

import getGamePlayers from "../services/getGamePlayers";
import Disconectgamestarted from "../services/DisconectGameStarte";
import deleteGame from "../services/deleteGame";
import handleMovement from "../services/handleMovement";
import handleFigura from "../services/handleFigura";
import handleFiguraBlock from "../services/handleFiguraBlock";
import getWinner from "../services/getWinner";
import handleCancelMovement from "../services/handleCancelMovement";

import SideMenu from "../../lobby/containers/SideMenu";
import RenderTables from "./RenderTables";
import emitter from "../services/eventEmitter";

const Game = ({ socket }) => {
  const navigate = useNavigate();
  const partida_id = sessionStorage.getItem("partida_id");
  const [players, setPlayers] = useState([]); // Modificador de jugadores
  const [winner, setWinner] = useState({ id_player: "", name: "" }); // Estado para guardar el ganador
  const [prevPlayers, setPrevPlayers] = useState([]);

  // Funcion para desconectar al jugador de la partida
  const Disconect = async () => {
    const player_id = sessionStorage.getItem("jugador_id");
    const sid = sessionStorage.getItem("sid");
    emitter.emit("log_JugadorDesconectado", player_id);
    await Disconectgamestarted(partida_id, player_id, sid, navigate);
  };

  // Funcion para desconectar al ultimo jugador de la partida
  const Disconect2 = async () => {
    const partida_id = sessionStorage.getItem("partida_id");
    const sid = sessionStorage.getItem("sid");
    const response = await deleteGame(partida_id, sid);
    if (response) {
      sessionStorage.removeItem("partida_id");
      sessionStorage.removeItem("partida_nombre");
      sessionStorage.removeItem("turnStartTime");
      navigate("/");
    }
  };

  // Función para obtener los jugadores de la partida
  const fetchPlayers = async () => {
    const jugadores = await getGamePlayers(partida_id);
    if (jugadores && jugadores.length > 0) {
      setPlayers(jugadores);
    } else {
      console.log("No hay jugadores disponibles.");
    }

    // Si prevPlayers está vacío, significa que es la primera vez que cargamos los jugadores
    if (prevPlayers.length === 0) {
      setPrevPlayers(jugadores); // Inicializa prevPlayers con los jugadores obtenidos
    } else {
      // Verifica si ha habido una desconexión (menos jugadores que antes)
      if (prevPlayers.length > jugadores.length) {
        const disconnectedPlayer = prevPlayers.find(
          (player) => !jugadores.some((j) => j.jugador_id === player.jugador_id)
        );

        // Emite el evento si se detecta un jugador desconectado
        if (disconnectedPlayer) {
          console.log(
            "Emitiendo jugador desconectado: ",
            disconnectedPlayer.jugador_id
          );
          emitter.emit(
            "log_JugadorDesconectado",
            disconnectedPlayer.jugador_id
          );
        }
      }
    }

    setPrevPlayers(jugadores);
    setPlayers(jugadores);
  };

  const fetchWinner = async () => {
    const ganador = await getWinner(partida_id);
    if (ganador.id_player !== "") {
      setWinner(ganador);
      console.log("hubo ganador: ", ganador.name);
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      await fetchPlayers();
      await fetchWinner();
    };

    fetchData();

    socket.on("jugador_gana", fetchWinner);
    socket.on("jugador_abandona_ini", fetchPlayers);

    return () => {
      socket.off("jugador_gana", fetchWinner);
      socket.off("jugador_abandona_ini", fetchPlayers);
    };
  }, [socket, partida_id]);

  useEffect(() => {
    handleFigura();
    handleFiguraBlock();
    handleMovement(); // Inicia la escucha de eventos de botones para movimiento
    handleCancelMovement(); //Inicio la escucha de evento del boton cancelar movimiento
  }, []);

  return (
    <div className="game-container">
      <Grid
        container
        direction={"column"}
        spacing={2}
        justifyContent="center"
        alignItems="center"
      >
        {/* Verifica que players no esté vacío antes de pasar como prop */}
        {players.length > 0 && socket != null ? (
          <RenderTables
            players={players}
            Disconect={Disconect}
            Disconect2={Disconect2}
            socket={socket}
            winner={winner}
          />
        ) : (
          <Typography variant="h4">Cargando jugadores...</Typography>
        )}
      </Grid>
    </div>
  );
};

export default Game;
