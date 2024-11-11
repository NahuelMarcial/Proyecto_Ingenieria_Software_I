import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Typography, Box, Paper } from "@mui/material";
import HappyFace from "../../assets/icons/HappyFace";
import AngryFace from "../../assets/icons/AngryFace";

import PlayerList from "../components/PlayerList";
import BotonAbandonarPartida from "../components/BotonAbandonarPartida";
import StartGameButton from "../components/StartGameButton";
import OwnerLeftDialog from "../components/OwnerLeaveDialog";
import Loading from "../components/Loading";
import SideMenu from "./SideMenu";
import { BackToHome } from "../../principal/components/BackToButtons";

import getPlayerListService from "../services/getPlayerListService";
import getNamesPlayers from "../services/getNamesPlayers";
import abandonarPartida from "../services/abandonarPartida";
import startGame from "../services/StartGame";
import newSetFigCards from "../services/newSetFigCards";
import newSetMovCards from "../services/newSetMovCards";
import newSetFichas from "../services/newSetFichas";
import getOwner from "../services/getOwner";
import deleteGame from "../../game/services/deleteGame";
import getMaxPlayers from "../services/getMaxPlayers";
import getDifficult from "../../game/services/getDifficult";

function Lobby({ socket }) {
  const navigate = useNavigate();
  const [players, setJugadores] = useState([]);
  const [maxPlayers, setMaxPlayers] = useState(0);
  const [playersNames, setPlayersNames] = useState([]);
  const [playersCount, setPlayersCount] = useState(0);
  const [ownerId, setOwnerId] = useState(null);
  const [isOwnerLeave, setOwnerLeave] = useState(false);

  const isDifficult = getDifficult();
  const partida_id = sessionStorage.getItem("partida_id");
  const partida_nombre = sessionStorage.getItem("partida_nombre");
  const jugador_id = sessionStorage.getItem("jugador_id");

  const getPlayers = async () => {
    const players = await getPlayerListService(partida_id);
    const playersNames = await getNamesPlayers(partida_id);
    setJugadores(players);
    setPlayersNames(playersNames);
    const count = Object.values(players).filter((player) => player !== "");
    setPlayersCount(count.length);
  };

  const fetchMaxPlayers = async () => {
    const maxPlayers = await getMaxPlayers();
    setMaxPlayers(maxPlayers);
  };

  const fetchOwner = async () => {
    const owner = await getOwner(partida_id);
    setOwnerId(owner.owner);
  };

  useEffect(() => {
    getPlayers();
    fetchMaxPlayers();
    fetchOwner();

    socket.on("jugador_unido_lobby", (data) => {
      getPlayers();
    });

    socket.on("jugador_abandona_lobby_noini", () => {
      getPlayers();
    });

    socket.on("partida_iniciada_lobby", async (data) => {
      getPlayers();
      if (Number(data.partida_id) === Number(partida_id)) {
        navigate(`/game/${partida_id}`);
      }
    });

    socket.on("owner_abandona_lobby", (data) => {
      fetchOwner();
      getPlayers();
    });

    return () => {
      socket.off("jugador_unido_lobby");
      socket.off("jugador_abandona_lobby_noini");
      socket.off("partida_iniciada_lobby");
      socket.off("owner_abandona_lobby");
    };
  }, []);

  useEffect(() => {
    if (ownerId === "") {
      setOwnerLeave(true);
    }
  }, [ownerId]);

  const isOwner = ownerId === jugador_id;

  const Disconect = async () => {
    const player_id = sessionStorage.getItem("jugador_id");
    const sid = sessionStorage.getItem("sid");
    let response;
    if (playersCount === 1) {
      response = await deleteGame(partida_id, sid);
    } else {
      response = await abandonarPartida(partida_id, player_id, sid);
    }

    if (response) {
      sessionStorage.removeItem("partida_id");
      sessionStorage.removeItem("partida_nombre");
      sessionStorage.removeItem("turnStartTime");
      navigate("/");
    }
  };

  const StartGame = async () => {
    const player_id = sessionStorage.getItem("jugador_id");
    await startGame(partida_id, player_id);
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
      border={"2px solid #ddd"} // Borde de 1px
      borderRadius={2} // Bordes redondeados
      margin={"auto"} // Centra el contenedor
      marginTop={1} // Margen superior
      sx={{
        height: { xs: "66vh", sm: "80vh", md: "86vh" }, // Altura mínima del contenedor
        width: { xs: "62%", sm: "56%", md: "52%" }, // Ancho máximo del contenedor
      }}
    >
      <Paper
        elevation={2}
        sx={{
          backgroundColor: "grey.200",
          padding: 1.5,
          minWidth: "50%",
          maxWidth: "90%",
          borderRadius: 1.5,
          marginTop: 0,
          marginBottom: { xs: 4, sm: 2, md: 1 },
          border: "1px solid #888",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <Box
          sx={{
            display: "inline-flex",
            alignItems: "center",
            justifyContent: "center",
            borderRadius: 2,
            bgcolor: "grey.100",
            border: 3,
            padding: 0,
          }}
        >
          {isDifficult ? (
            <AngryFace sx={{ fontSize: "2.5rem" }} />
          ) : (
            <HappyFace sx={{ fontSize: "2.5rem" }} />
          )}
        </Box>
        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          margin="auto"
          sx={{ marginLeft: 2 }}
        >
          <Typography variant="h2" color="primary.dark">
            {partida_nombre}
          </Typography>
        </Box>
      </Paper>

      <Box
        sx={{
          backgroundColor: "grey.200",
          padding: 1,
          borderRadius: 1,
          marginBottom: 0.5,
        }}
      >
        <Typography variant="h4" color="secondary.dark">
          Jugadores conectados:
        </Typography>
      </Box>
      <Box sx={{ width: "90%", height: { xs: "100%", sm: "80%", md: "68%" } }}>
        <PlayerList
          players={players}
          playersNames={playersNames}
          maxPlayers={maxPlayers}
        />
      </Box>

      {/* Contenedor para los botones en fila */}
      <Box
        display="flex"
        justifyContent="space-between"
        sx={{
          marginTop: { xs: 2, sm: 4, md: 6 },
          gap: { xs: "2vw", sm: "2vw", md: "4vw" },
        }}
      >
        <Box>
          <BotonAbandonarPartida onClick={Disconect} />
        </Box>
        <Box>
          <BackToHome />
        </Box>
        <Box>
          <SideMenu />
        </Box>
        <Box>
          <StartGameButton
            onClick={StartGame}
            isOwner={isOwner}
            isAvailable={playersCount > 1}
          />
        </Box>
      </Box>
      <OwnerLeftDialog open={isOwnerLeave} onClose={Disconect} />

      {/* Mostrar Loading si hay lugar*/}
      {!(maxPlayers === playersCount) && <Loading />}
    </Box>
  );
}

export default Lobby;
