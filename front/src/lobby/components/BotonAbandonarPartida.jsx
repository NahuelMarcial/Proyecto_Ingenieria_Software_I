import React from "react";
import { Button } from "@mui/material";

const BotonAbandonarPartida = ({ onClick }) => {
  return (
    <Button
      onClick={onClick}
      style={{ float: "right" }}
      sx={{
        backgroundColor: "error.main",
        color: "white",
        border: 1,
        borderColor: "error.dark",
        fontSize: 16,
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: "error.light",
        },
      }}
    >
      Abandonar Partida
    </Button>
  );
};

export default BotonAbandonarPartida;
