import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Typography, Box } from "@mui/material";

import PlayerList from "../components/PlayerList";
import BotonAbandonarPartida from "../components/BotonAbandonarPartida";
import StartGameButton from "../components/StartGameButton";

import getPlayerListService from "../services/getPlayerListService";
import abandonarPartida from "../services/abandonarPartida";
import startGame from "../services/StartGame";
import newSetFigCards from "../services/newSetFigCards";
import newSetMovCards from "../services/newSetMovCards";
import newSetFichas from "../services/newSetFichas";
import getOwner from "../services/getOwner";

function Lobby({ socket }) {
  const navigate = useNavigate();
  const [players, setJugadores] = useState([]);
  const partida_id = sessionStorage.getItem("partida_id");
  const partida_nombre = sessionStorage.getItem("partida_nombre");
  const jugador_id = sessionStorage.getItem("jugador_id");
  const [ownerId, setOwnerId] = useState(null);

  const getPlayers = async () => {
    const players = await getPlayerListService(partida_id); // llamada a la API
    setJugadores(players);
    sessionStorage.setItem("players", JSON.stringify(players));
  };

  const fetchOwner = async () => {
    const owner = await getOwner(partida_id); // Obtiene el owner de la partida
    console.log("owner", owner);
    setOwnerId(owner.owner); // Suponiendo que el owner tiene una propiedad id
  };

  useEffect(() => {
    getPlayers(); // primera vez
    fetchOwner(); // Obtener el owner

    // escuchar evento jugador_unido_lobby para actualizar la lista de jugadores
    socket.on("jugador_unido_lobby", (data) => {
      console.log("jugador_unido_lobby", data);
      getPlayers();
    });

    socket.on("jugador_abandona_lobby_noini", () => {
      getPlayers();
    });

    socket.on("partida_iniciada_lobby", async (data) => {
      console.log("juego iniciado", data);
      getPlayers(); // obtengo la lista de jugadores actualizada con el orden de los turnos
      const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

      await sleep(600); // sleep for 2 seconds
      navigate(`/game/${partida_id}`);
    });

    return () => {
      socket.off("jugador_unido_lobby");
      socket.off("jugador_abandona_lobby_noini");
      socket.off("partida_iniciada_lobby");
    };
  }, []);

  const isOwner = ownerId === jugador_id;
  console.log("isOwner", isOwner);

  const Disconect = () => {
    const player_id = sessionStorage.getItem("jugador_id");
    const sid = sessionStorage.getItem("sid");
    const response = abandonarPartida(partida_id, player_id, sid, navigate);
    if (response.ok) {
      sessionStorage.removeItem("partida_id");
      sessionStorage.removeItem("partida_nombre");
      sessionStorage.removeItem("players");
    }
  };

  const StartGame = async () => {
    const player_id = sessionStorage.getItem("jugador_id");
    await startGame(partida_id, player_id); // muy importante que este servicio este primero
    await newSetFigCards(partida_id);
    await newSetMovCards(partida_id);
    await newSetFichas(partida_id);
  };

  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
      bgcolor="grey.50" // Fondo gris claro
      padding={4} // Añade padding interno opcional
      maxWidth={600} // Ancho máximo del contenedor
      border={"1px solid #ddd"} // Borde de 1px
      borderRadius={2} // Bordes redondeados
      margin={"auto"} // Centra el contenedor
      marginTop={4} // Margen superior
    >
      <Typography variant="h2" color="primary.dark">
        Unido al Lobby: {partida_nombre}
      </Typography>
      <Typography variant="h4" color="secondary.dark" marginBottom={2}>
        Jugadores conectados:
      </Typography>
      <PlayerList players={players} />

      {/* Contenedor para los botones en fila */}
      <Box display="flex" justifyContent="center" marginTop={2} gap={20}>
        <BotonAbandonarPartida onClick={Disconect} />
        <StartGameButton onClick={StartGame} isOwner={isOwner} />
      </Box>
    </Box>
  );
}

export default Lobby;
