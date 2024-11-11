import React from "react";
import { Button, Box } from "@mui/material";

const BotonAbandonarPartida = ({ onClick }) => {
  return (
    <Button
      onClick={onClick}
      sx={{
        width: "100%",
        height: "100%",
        paddingRight: 0,
        paddingLeft: 0,
        backgroundColor: "error.main",
        color: "white",
        border: 1,
        borderColor: "error.dark",
        fontSize: "clamp(0.6rem, 1.5vw, 1.5rem)",
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
