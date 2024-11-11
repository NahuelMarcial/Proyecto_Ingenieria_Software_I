import React from "react";
import { Button } from "@mui/material";

const StartGameButton = ({ onClick, isOwner, isAvailable }) => {
  const isButtonEnabled = isOwner && isAvailable;

  return (
    <Button
      sx={{
        width: "100%",
        height: "100%",
        backgroundColor: isButtonEnabled ? "success.main" : "grey.400",
        color: "white",
        border: 1,
        borderColor: isButtonEnabled ? "success.dark" : "grey.500",
        fontSize: "clamp(0.6rem, 1.5vw, 1.5rem)",
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: isButtonEnabled ? "success.light" : "grey.500",
        },
        opacity: isButtonEnabled ? 1 : 0.6,
      }}
      onClick={onClick}
      disabled={!isButtonEnabled}
    >
      Iniciar Juego
    </Button>
  );
};

export default StartGameButton;
