import React, { useState } from "react";
import HappyFace from "../../assets/icons/HappyFace";
import AngryFace from "../../assets/icons/AngryFace";
import { Box, Button, Typography } from "@mui/material";

const SwitchDifficulty = ({ onChange }) => {
  const [isDifficult, setIsDifficult] = useState(false);

  const handleToggle = () => {
    const newValue = !isDifficult;
    setIsDifficult(newValue);
    if (onChange) {
      onChange(newValue);
    }
  };

  return (
    <div>
      <Typography
        variant="body2"
        color="text.secondary"
        sx={{
          ml: 1,
          fontSize: { xs: "0.7rem", sm: "0.9rem" },
          marginBottom: 1,
        }}
      >
        Dificultad
      </Typography>
      <Box
        marginLeft={0.5}
        sx={{
          display: "flex",
          alignItems: "center",
          border: "2px solid",
          borderColor: "#bbb",
          borderRadius: 1,
          width: "95%",
          padding: 0.3,
        }}
      >
        <Box
          sx={{
            position: "absolute",
            width: "50%",
            display: "flex",
            paddingRight: "10%",
            paddingLeft: "10%",
            justifyContent: "space-between",
          }}
        >
          <Typography
            color="error.main"
            sx={{ fontWeight: "bold", fontSize: "130%" }}
          >
            Difícil
          </Typography>

          <Typography
            color="success.main"
            sx={{ fontWeight: "bold", fontSize: "130%" }}
          >
            Fácil
          </Typography>
        </Box>
        <Button
          onClick={handleToggle}
          variant="outlined"
          color="grey"
          sx={{
            width: "50%", // Ocupa la mitad del contenedor
            border: "2px solid",
            borderColor: isDifficult ? "error.dark" : "success.dark",
            borderRadius: 1,
            backgroundColor: isDifficult ? "error.main" : "success.main",
            transition: "margin-left 0.3s ease-in-out",
            marginLeft: isDifficult ? "50%" : "0", // Se mueve al 50% o vuelve a 0%
          }}
        >
          {isDifficult ? (
            <AngryFace sx={{ fontSize: "2rem" }} />
          ) : (
            <HappyFace sx={{ fontSize: "2rem" }} />
          )}
        </Button>
      </Box>
    </div>
  );
};

export default SwitchDifficulty;
