import React from "react";
import { Box, Typography } from "@mui/material";
import Grid from "@mui/material/Grid2";
import TableroInfo from "./TableroInfo";
import PlayerHandContainer from "./PlayerHandContainer";
import BotonAbandonarPartida from "../../lobby/components/BotonAbandonarPartida";
import Winner from "../components/Winer";

const RenderTables = ({ players, fichas, Disconect, Disconect2, socket }) => {
  const playerCount = players.length;

  if (playerCount === 1) {
    // Un solo jugador: solo se muestra su mano
    return (
      <Box>
        <Typography variant="h2">FELICIDADES, GANASTE LA PARTIDA!!!</Typography>
        <Winner win={true} handleClose={Disconect2} />
      </Box>
    );
  } else if (playerCount === 2) {
    // Dos jugadores: uno enfrente del otro con el tablero en el medio
    return (
      <>
        <Grid item="true" xs={12} display="flex" justifyContent="center">
          <PlayerHandContainer jugador={players[1]} /> {/* Jugador 1 */}
        </Grid>
        <Grid item="true" xs={12} display="flex" justifyContent="center">
          <TableroInfo players={players} fichas={fichas} socket={socket} />
        </Grid>
        <Grid item="true" xs={12} display="flex" justifyContent="center">
          <PlayerHandContainer jugador={players[0]} /> {/* Jugador 2 */}
        </Grid>
        <BotonAbandonarPartida onClick={Disconect} />
      </>
    );
  } else if (playerCount === 3) {
    // Tres jugadores: uno abajo y dos en los costados
    return (
      <>
        <Grid
          container
          xs={12}
          spacing={2}
          justifyContent="center"
          alignContent="center"
        >
          <Grid item="true" xs={4} display="flex" justifyContent="center">
            <PlayerHandContainer jugador={players[1]} /> {/* Jugador 1 */}
          </Grid>
          <Grid item="true" xs={4} display="flex" justifyContent="center">
            <TableroInfo players={players} fichas={fichas} socket={socket} />
          </Grid>
          <Grid item="true" xs={4} display="flex" justifyContent="center">
            <PlayerHandContainer jugador={players[2]} /> {/* Jugador 2 */}
          </Grid>
        </Grid>
        <Grid item="true" xs={12} display="flex" justifyContent="center">
          <PlayerHandContainer jugador={players[0]} /> {/* Jugador 3 */}
        </Grid>
        <BotonAbandonarPartida onClick={Disconect} />
      </>
    );
  } else if (playerCount === 4) {
    // Cuatro jugadores: todos alrededor del tablero
    return (
      <>
        <Grid item="true" xs={12} display="flex" justifyContent="center">
          <PlayerHandContainer jugador={players[2]} /> {/* Jugador 2 */}
        </Grid>
        <Grid
          container
          xs={12}
          spacing={2}
          justifyContent="center"
          alignContent="center"
        >
          <Grid item="true" xs={4} display="flex" justifyContent="center">
            <PlayerHandContainer jugador={players[1]} /> {/* Jugador 1 */}
          </Grid>
          <Grid item="true" xs={4} display="flex" justifyContent="center">
            <TableroInfo players={players} fichas={fichas} socket={socket} />
          </Grid>
          <Grid item="true" xs={4} display="flex" justifyContent="center">
            <PlayerHandContainer jugador={players[3]} /> {/* Jugador 3 */}
          </Grid>
        </Grid>
        <Grid item="true" xs={12} display="flex" justifyContent="center">
          <PlayerHandContainer jugador={players[0]} /> {/* Jugador 4 */}
        </Grid>
        <BotonAbandonarPartida onClick={Disconect} />
      </>
    );
  }
};

export default RenderTables;
