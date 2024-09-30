import React, { useEffect, useState } from "react";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import { Button } from "@mui/material";
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

const Winer = ({ win, handleClose }) => {
  const [playerName, setPlayerName] = useState("");

  useEffect(() => {
    const name = sessionStorage.getItem("jugador_nombre");
    setPlayerName(name || "Unknown Player");
  }, []);

  return (
    <StyledDialog open={win} onClose={handleClose}>
      <DialogTitle>
        <CelebrationIcon style={{ fontSize: 50 }} />{" "}
        {/* Icono de celebración */}
        <div>Felicidades {playerName}!!!</div>
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

export default Winer;
