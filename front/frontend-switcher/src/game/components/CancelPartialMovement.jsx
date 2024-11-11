import React from "react";
import { Button } from "@mui/material";

const CancelPartialMovement = ({ onclick, isTurn }) => {
  return (
    <Button
      variant="contained"
      sx={{
        width: 136,
        height: 35,
        backgroundColor: "success.main",
        color: "white",
        border: 1,
        fontSize: 14,
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: "success.light",
        },
      }}
      onClick={onclick}
      disabled={!isTurn}
    >
      Retroceder
    </Button>
  );
};

export default CancelPartialMovement;
