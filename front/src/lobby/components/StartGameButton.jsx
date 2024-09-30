import React from "react";
import { Button } from "@mui/material";

const StartGameButton = ({ onClick, isOwner }) => {
  return (
    <Button
      style={{ float: "right" }}
      sx={{
        backgroundColor: isOwner ? "success.main" : "grey.400", // Cambia el color de fondo según el estado
        color: "white",
        border: 1,
        borderColor: isOwner ? "success.dark" : "grey.500", // Cambia el color del borde según el estado
        fontSize: 16,
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: isOwner ? "success.light" : "grey.500", // Cambia el color al pasar el mouse
        },
        opacity: isOwner ? 1 : 0.6, // Cambia la opacidad según el estado
      }}
      onClick={onClick}
      disabled={!isOwner}
    >
      Iniciar Juego
    </Button>
  );
};

export default StartGameButton;
