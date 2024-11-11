import React from "react";
import Button from "@mui/material/Button";
import { Box, Typography } from "@mui/material";

const CreateGameButton = ({ onClick }) => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        padding: 1,
        margin: "0 auto",
      }}
    >
      <Button
        variant="contained"
        color="success"
        onClick={onClick}
        sx={{
          padding: {
            xs: "8px 20px",
            sm: "10px 24px",
            md: "10px 32px",
          },
          width: "70%",
          height: {
            xs: "50px",
            sm: "65px",
            md: "80px",
          },
          transition: "transform 0.3s, box-shadow 0.3s",
          "&:hover": {
            bgcolor: "success.light",
            transform: "scale(1.05)",
            boxShadow: "5px 5px 2px rgba(0, 0, 0, 0.4);",
          },
        }}
      >
        <Typography variant="h2">CREAR PARTIDA</Typography>
      </Button>
    </Box>
  );
};

export default CreateGameButton;
