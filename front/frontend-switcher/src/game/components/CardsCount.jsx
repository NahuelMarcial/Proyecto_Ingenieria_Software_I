import React, { useEffect, useState } from "react";
import { Box, Card, CardContent, Typography } from "@mui/material";
import DeckIcon from "../../assets/icons/DeckIcon";
import GetCardsCount from "../services/GetCardsCount";

const CardsCount = ({ socket }) => {
  const [showdeck, setShowDeck] = useState(true);
  const [ammountCard, setAmmountCard] = useState(0);
  const gameid = sessionStorage.getItem("partida_id");
  const playerid = sessionStorage.getItem("jugador_id");

  useEffect(() => {
    const getCountCards = async () => {
      const data = await GetCardsCount(gameid, playerid);
      setAmmountCard(data.cantidad);
      setShowDeck(data.cantidad > 0);
    };

    getCountCards();

    const handleSetCartasFiguraCreado = async () => {
      await getCountCards();
    };

    const handleTurnoPasado = async () => {
      await getCountCards();
    };

    socket.on("set_cartas_figura_creado", handleSetCartasFiguraCreado);
    socket.on("turno_pasado", handleTurnoPasado);

    return () => {
      socket.off("set_cartas_figura_creado", handleSetCartasFiguraCreado);
      socket.off("turno_pasado", handleTurnoPasado);
    };
  }, [socket]);

  return (
    <Box position="relative">
      {showdeck && <DeckIcon data-testid="deckicon" sx={{ fontSize: 100 }} />}
      {showdeck && (
        <Typography
          position="absolute"
          top="40%"
          left="43%"
          transform="translate(-50%, -50%)"
          variant="h2"
        >
          {ammountCard}
        </Typography>
      )}
    </Box>
  );
};

export default CardsCount;
