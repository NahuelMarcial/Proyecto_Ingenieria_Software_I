import React, { useEffect, useState } from "react";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import { Button, Typography } from "@mui/material";
import { styled } from "@mui/system";
import CelebrationIcon from "@mui/icons-material/EmojiEvents"; // Importa un ícono de celebración

const StyledDialog = styled(Dialog)(({ theme }) => ({
  "& .MuiDialogTitle-root": {
    backgroundColor: "#4caf50", // Fondo verde
    color: "white",
    fontSize: "24px",
    textAlign: "center",
    padding: theme.spacing(2),
  },
  "& .MuiDialog-paper": {
    padding: theme.spacing(2),
    borderRadius: "8px",
  },
}));

const Winner = ({ win, handleClose, winner }) => {
  console.log("winner: ", winner);
  const playerName = winner.name;
  const currentPlayerId = sessionStorage.getItem("jugador_id");

  return (
    <StyledDialog open={win} onClose={handleClose}>
      <DialogTitle variant="h3">
        <CelebrationIcon style={{ fontSize: 50 }} />{" "}
        {/* Icono de celebración */}
        {currentPlayerId === winner.id_player ? (
          <div>Felicidades {playerName}, ganaste!!!</div>
        ) : (
          <div> El ganador es {playerName}!!!</div>
        )}
      </DialogTitle>
      <Button
        variant="contained"
        color="primary"
        onClick={handleClose}
        style={{ marginTop: "20px" }}
        sx={{ fontSize: 20 }}
      >
        Salir
      </Button>
    </StyledDialog>
  );
};

export default Winner;
