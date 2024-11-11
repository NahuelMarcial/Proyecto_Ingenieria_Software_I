import React, {useEffect, useState} from "react";
import {Box, Typography, Stack} from "@mui/material";
import Grid from "@mui/material/Grid2";

import FigureCard from "./FigureCard";
import MovCard from "./MovCard";
import SaltarTurno from "./SaltarTurno";
import CancelPartialMovement from "./CancelPartialMovement";

import emitter from "../services/eventEmitter";
import {endTurn} from "../services/turnoService";
import getNameById from "../services/getNameById";
import CardsCount from "./CardsCount";

const PlayerHand = ({
                      jugador_id,
                      isHost,
                      figureCards = [],
                      movCards = [],
                      isTurn,
                      width,
                      height,
                      socket
                    }) => {
  const [selectedMovCard, setSelectedMovCard] = useState(null);
  const [selectedFigCard, setSelectedFigCard] = useState(null);

  const [movCardDisabled, setMovCardDisabled] = useState(false);
  const [figCardDisabled, setFigCardDisabled] = useState(false);

  const partida_id = sessionStorage.getItem("partida_id");
  const [name, setName] = useState("");

  // Función para obtener el nombre del jugador por su ID
  const getName = async (id) => {
    const name = await getNameById(id);
    setName(name);
  };

  // Manejar la acción de "Saltar Turno"
  const handleSkipTurn = async () => {
    emitter.emit("log_TurnoSaltadoPorBotón", jugador_id);
    await endTurn(partida_id, jugador_id);
  };

  const handleMovCardClick = (card_id) => {
    if (movCardDisabled) {
      console.log(
        "No se pueden seleccionar cartas de movimiento mientras haya una carta de figura seleccionada."
      );
      return;
    }

    if (selectedMovCard === card_id) {
      // Si la misma carta es clickeada nuevamente, se deselecciona
      setSelectedMovCard(null);
      setFigCardDisabled(false);
      emitter.emit("movCardSelected", null);
      emitter.emit("movCardClicked", false); // Emitir false cuando se deselecciona
      console.log(`Carta movimiento ${card_id} deseleccionada`);
    } else {
      // Si es una nueva carta, seleccionarla
      setSelectedMovCard(card_id);
      setFigCardDisabled(true);
      emitter.emit("movCardSelected", card_id);
      emitter.emit("movCardClicked", true); // Emitir true cuando se selecciona
      console.log(`Carta movimiento ${card_id} seleccionada`);
    }
  };

  const handleFigCardClick = (figure) => {
    if (figCardDisabled) {
      console.log(
        "No se pueden seleccionar cartas de figura mientras haya una carta de movimiento seleccionada."
      );
      return;
    }

    if (selectedFigCard === figure.id_carta) {
      setSelectedFigCard(null);
      setMovCardDisabled(false);
      emitter.emit("figCardClicked", false);

      if (figure.id_player === sessionStorage.getItem("jugador_id")) {
        emitter.emit("figCardSelected", null);
      } else {
        emitter.emit("figCardSelectedForBlock", null); // Emitir null para deseleccionar
      }
      console.log(`Carta figura ${figure.id_carta} deseleccionada`);
    } else {
      setSelectedFigCard(figure.id_carta);
      setMovCardDisabled(true);
      emitter.emit("figCardClicked", true);

      if (figure.id_player === sessionStorage.getItem("jugador_id")) {
        console.log("La carta figura pertenece al host.");
        emitter.emit("figCardSelected", figure.id_carta);
        console.log(`Carta figura ${figure.id_carta} seleccionada`);
      } else {
        console.log("La carta figura NO pertenece al host.");
        emitter.emit("figCardSelectedForBlock", figure.id_carta); // Emitir id_carta para seleccionar
        console.log(`Carta figura ${figure.id_carta} seleccionada`);
      }
    }
  };

  const handleCancelMovement = () => {
    emitter.emit("CancelMovement", jugador_id);
  };

  useEffect(() => {
    getName(jugador_id);

    emitter.on("movCancelado", () => {
      setSelectedMovCard(null);
      setMovCardDisabled(false);
      setFigCardDisabled(false);
      emitter.emit("movCardClicked", false);
    });

    emitter.on("figCancelado", () => {
      setSelectedFigCard(null);
      setMovCardDisabled(false);
      setFigCardDisabled(false);
      emitter.emit("figCardClicked", false);
    });

    return () => {
      emitter.off("movCancelado");
      emitter.off("figCancelado");
    };
  }, []);

  return (
    <Box
      sx={{
        width, // Usar el valor de width
        height, // Usar el valor de height
        padding: 1,
        borderRadius: 2,
        border: isTurn ? "5px  solid" : "3px solid",
        borderColor: isTurn ? "#1889bb" : "#ddd",
        bgcolor: isTurn ? "secondary.main" : "#f8f9fa",
      }}
    >
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between", // Ajustar el espacio entre ambos
          alignItems: "center", // Alinear verticalmente
          marginBottom: 1, // Espacio debajo del contenedor
        }}
      >
        <Typography marginLeft={2} variant="h3">
          {name}
        </Typography>
        {isHost && (
          <Stack direction="row" spacing={2}>
            <CancelPartialMovement
              onclick={handleCancelMovement}
              isTurn={isTurn}
            />
            <SaltarTurno handleSkipTurn={handleSkipTurn} isTurn={isTurn}/>
          </Stack>
        )}
      </Box>
      <Grid
        container
        spacing={2}
        display="flex"
        justifyContent="center"
        alignItems="center"
      >
        {/* Mostrar siempre las cartas de figura */}
        {figureCards.map((figure, index) => (
          <Grid key={index}>
            <FigureCard
              imageSrc={figure.imageSrc}
              title={figure.title}
              isClicked={selectedFigCard === figure.id_carta} // Indicar si está seleccionada
              isBlocked={figure.bloqueada} // Indicar si está bloqueada
              isForBlock={
                figure.id_player !== sessionStorage.getItem("jugador_id")
              }
              onClick={() => handleFigCardClick(figure)} // Manejar selección
            />
          </Grid>
        ))}

        {/* Mostrar cartas de movimiento solo si es host */}
        {isHost &&
          movCards.map((mov, index) => (
            <Grid key={index}>
              <MovCard
                imageSrc={mov.imageSrc}
                title={mov.title}
                idMov={mov.id_carta}
                isClicked={selectedMovCard === mov.id_carta}
                onClick={() => handleMovCardClick(mov.id_carta)}
                gastada={mov.gastada}
              />
            </Grid>
          ))}
        <CardsCount socket={socket}/>
      </Grid>
    </Box>
  );
};

export default PlayerHand;
