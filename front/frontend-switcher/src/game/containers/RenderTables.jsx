import React, { useMemo } from "react";
import { Box, Typography } from "@mui/material";
import Grid from "@mui/material/Grid2";
import TableroInfo from "./TableroInfo";
import PlayerHandContainer from "./PlayerHandContainer";
import Chat from "./Chat";
import BotonAbandonarPartida from "../../lobby/components/BotonAbandonarPartida";
import Winner from "../components/Winner";
import PlayerDisconnect from "../components/PlayerDisconnect";
import { BackToHome } from "../../principal/components/BackToButtons";
import SideMenu from "../../lobby/containers/SideMenu";

const RenderTables = ({ players, Disconect, Disconect2, socket, winner }) => {
  const jugadorId = sessionStorage.getItem("jugador_id");

  const reorderedPlayers = useMemo(() => {
    if (players.length === 0) return [];
    const currentPlayerIndex = players.findIndex(
      (player) => player === jugadorId
    );

    return [
      players[currentPlayerIndex],
      ...players.slice(currentPlayerIndex + 1),
      ...players.slice(0, currentPlayerIndex),
    ];
  }, [players, jugadorId]);

  const playerCount = players.length;

  // Renderiza las tablas según la cantidad de jugadores
  if (winner.id_player !== "") {
    // Hay ganador: muestra pestaña emergente de ganador
    console.log("cantidad de jugadores", playerCount);
    const handleClose = playerCount > 1 ? Disconect : Disconect2;

    return (
      <Box>
        <Typography variant="h2">HAY GANADOR!!!</Typography>
        <Winner win={true} handleClose={handleClose} winner={winner} />
      </Box>
    );
  } else if (playerCount === 1) {
    // Un solo jugador: muestra pestaña emergente de ganador
    return (
      <Box>
        <Typography variant="h2">FELICIDADES, GANASTE LA PARTIDA!!!</Typography>
        <Winner win={true} handleClose={Disconect2} winner={winner} />
      </Box>
    );
  } else if (playerCount === 2) {
    return (
      <Grid
        container
        rowSpacing={1}
        columnSpacing={{ xs: 1, sm: 2, md: 3 }}
        marginTop={1}
      >
        {/* Fila de arriba (Otros jugadores y tablero)*/}
        <Grid container size={12} display="flex" alignItems="center">
          {/* Jugador Este (desconetado) */}
          <Grid
            container
            size={3}
            height="100%"
            justifyContent="flex-end" // Alinea a la derecha
            alignItems="flex-end" // Alinea hacia abajo
            display="flex"
          >
            <SideMenu />
            <PlayerDisconnect socket={socket} width={150} height={437} />
          </Grid>

          <Grid container size={6} justifyContent="center" display="flex">
            {/* Jugador Norte (1) */}
            <Grid
              size={12}
              display="flex"
              justifyContent="center"
              alignItems="flex"
            >
              <PlayerHandContainer
                jugador={reorderedPlayers[1]}
                socket={socket}
                width={550}
                height={145}
              />{" "}
            </Grid>
            {/* Tablero */}
            <Grid size={12} display="flex" justifyContent="center">
              <TableroInfo players={reorderedPlayers} socket={socket} />
            </Grid>
          </Grid>

          {/* Jugador Oeste (desconetado) */}
          <Grid
            container
            size={3}
            height="100%"
            justifyContent="flex-start"
            alignItems="flex-end"
            display="flex"
          >
            <PlayerDisconnect width={150} height={437} />
          </Grid>
        </Grid>

        {/* Fila de abajo (Jugador Host, chat y botones)*/}
        <Grid container size={12} marginTop={1}>
          <Grid
            size={3}
            display="flex"
            justifyContent="center"
            alignItems="center"
          >
            <Chat socket={socket} jugadorId={jugadorId} />
          </Grid>
          <Grid size={6} display="flex" justifyContent="center">
            {reorderedPlayers.length > 0 && (
              <PlayerHandContainer
                jugador={reorderedPlayers[0]}
                socket={socket}
                width="90%"
              />
            )}
          </Grid>
          {/* Botones Abandonar / Volver*/}
          <Grid size={2} justifyContent="center" alignContent="center">
            <Box display="flex" flexDirection="column" gap={2}>
              <BackToHome />
              <BotonAbandonarPartida onClick={Disconect} />
            </Box>
          </Grid>
        </Grid>
      </Grid>
    );
  } else if (playerCount === 3) {
    return (
      <Grid
        container
        rowSpacing={1}
        columnSpacing={{ xs: 1, sm: 2, md: 3 }}
        marginTop={1}
      >
        {/* Fila de arriba (Otros jugadores y tablero)*/}
        <Grid container size={12} display="flex" alignItems="center">
          {/* Jugador Este (2) */}
          <Grid
            container
            size={3}
            height="100%"
            justifyContent="flex-end"
            alignItems="flex-end"
            display="flex"
          >
            <SideMenu />
            <PlayerHandContainer
              jugador={reorderedPlayers[2]}
              socket={socket}
              width={150}
            />
          </Grid>

          <Grid container size={6} justifyContent="center" display="flex">
            {/* Jugador Norte (desconectado) */}
            <Grid
              size={12}
              display="flex"
              justifyContent="center"
              alignItems="flex"
            >
              <PlayerDisconnect width={550} height={145} />{" "}
            </Grid>
            {/* Tablero */}
            <Grid size={12} display="flex" justifyContent="center">
              <TableroInfo players={reorderedPlayers} socket={socket} />
            </Grid>
          </Grid>

          {/* Jugador Oeste (1) */}
          <Grid
            container
            size={3}
            height="100%"
            justifyContent="flex-start" // Alinea a la izquierda
            alignItems="flex-end" // Alinea hacia abajo
            display="flex"
          >
            <PlayerHandContainer
              jugador={reorderedPlayers[1]}
              socket={socket}
              width={150}
            />
          </Grid>
        </Grid>

        {/* Fila de abajo (Jugador Host, chat y botones)*/}
        <Grid container size={12} marginTop={1}>
          <Grid
            size={2}
            display="flex"
            justifyContent="center"
            alignItems="center"
          >
            <Chat socket={socket} jugadorId={jugadorId} />
          </Grid>
          <Grid size={8} display="flex" justifyContent="center">
            {reorderedPlayers.length > 0 && (
              <PlayerHandContainer
                jugador={reorderedPlayers[0]}
                socket={socket}
                width={850}
              />
            )}
          </Grid>
          {/* Botones Abandonar / Volver*/}
          <Grid size={2} justifyContent="center" alignContent="center">
            <Box display="flex" flexDirection="column" gap={2}>
              <BackToHome />
              <BotonAbandonarPartida onClick={Disconect} />
            </Box>
          </Grid>
        </Grid>
      </Grid>
    );
  } else if (playerCount === 4) {
    return (
      <Grid
        container
        rowSpacing={1}
        columnSpacing={{ xs: 1, sm: 2, md: 3 }}
        marginTop={1}
      >
        {/* Fila de arriba (Otros jugadores y tablero)*/}
        <Grid container size={12} display="flex" alignItems="center">
          {/* Jugador Este (3) */}
          <Grid
            container
            size={3}
            height="100%"
            justifyContent="flex-end" // Alinea a la derecha
            alignItems="flex-end" // Alinea hacia abajo
            display="flex"
          >
            <SideMenu />
            <PlayerHandContainer
              jugador={reorderedPlayers[3]}
              socket={socket}
              width={150}
            />
          </Grid>

          <Grid container size={6} justifyContent="center" display="flex">
            {/* Jugador Norte (2) */}
            <Grid
              size={12}
              display="flex"
              justifyContent="center"
              alignItems="flex"
            >
              <PlayerHandContainer
                jugador={reorderedPlayers[2]}
                socket={socket}
                width={550}
                height={145}
              />{" "}
            </Grid>
            {/* Tablero */}
            <Grid size={12} display="flex" justifyContent="center">
              <TableroInfo players={reorderedPlayers} socket={socket} />
            </Grid>
          </Grid>

          {/* Jugador Oeste (1) */}
          <Grid
            container
            size={3}
            height="100%"
            justifyContent="flex-start" // Alinea a la izquierda
            alignItems="flex-end" // Alinea hacia abajo
            display="flex"
          >
            <PlayerHandContainer
              jugador={reorderedPlayers[1]}
              socket={socket}
              width={150}
            />
          </Grid>
        </Grid>

        {/* Fila de abajo (Jugador Host, chat y botones)*/}
        <Grid container size={12} marginTop={1}>
          <Grid
            size={3}
            display="flex"
            justifyContent="center"
            alignItems="center"
          >
            <Chat socket={socket} jugadorId={jugadorId} />
          </Grid>
          <Grid size={6} display="flex" justifyContent="center">
            {reorderedPlayers.length > 0 && (
              <PlayerHandContainer
                jugador={reorderedPlayers[0]}
                socket={socket}
                width="90%"
              />
            )}
          </Grid>
          {/* Botones Abandonar / Volver*/}
          <Grid size={3} justifyContent="center" alignContent="center">
            <Box display="flex" flexDirection="column" gap={2}>
              <BackToHome />
              <BotonAbandonarPartida onClick={Disconect} />
            </Box>
          </Grid>
        </Grid>
      </Grid>
    );
  }
};

export default RenderTables;
