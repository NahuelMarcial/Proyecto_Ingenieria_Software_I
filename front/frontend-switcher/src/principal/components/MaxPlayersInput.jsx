import React, { useState, useEffect } from "react";
import { Box, Button, IconButton, Typography } from "@mui/material";
import GroupsIcon from "@mui/icons-material/Groups2";

const MaxPlayersInput = ({ value, onChange }) => {
  const [isMaxPlayerSet, setIsMaxPlayerSet] = useState(false);

  const handleButtonClick = (numPlayers) => {
    onChange({ target: { name: "max_jugadores", value: numPlayers } });
  };

  useEffect(() => {
    setIsMaxPlayerSet(value > 0);
  }, [value]);

  return (
    <div>
      <Typography
        data-testid="title-max-players"
        variant="body2"
        color="text.secondary"
        sx={{ 
          ml: 1,
          fontSize: { xs: "0.7rem", sm: "0.9rem" }, 
        }}
      >
        Máximo de Jugadores *
      </Typography>
      <Box
        padding={1}
        gap={1.5}
        sx={{
          display: "flex",
          alignItems: "center",
        }}
      >
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            border: "2px solid",
            borderColor: isMaxPlayerSet ? "primary.main" : "#bbb",
            borderRadius: 1,
          }}
        >
          <IconButton disabled={true}>
            <GroupsIcon
              fontSize="large"
              sx={{ 
                color: isMaxPlayerSet ? "primary.main" : "#bbb",
                fontSize: { xs: "1.7rem", sm: "2.3rem" },  
              }}
            />
          </IconButton>
        </Box>
        <Box sx={{ display: "flex", justifyContent: "space-between", mt: 0 }}>
          {[2, 3, 4].map((num) => (
            <Button
              key={num}
              onClick={() => handleButtonClick(num)}
              variant={value === num ? "contained" : "outlined"}
              color="secondary"
              sx={{
                flex: 1,
                mx: { xs: 0.2, sm: 0.5 },  // Espacio horizontal entre botones
                boxShadow: 0,
                fontSize: { xs: 14.8, sm: 20 },  // Ajuste de tamaño de fuente
                width: { xs: 47, sm: 50 },  // Ancho adaptable
                height: { xs: 47, sm: 57 },
                fontWeight: "bold",
                borderWidth: 2,
                borderColor: value === num ? "secondary.main" : "#bbb",
                color: value === num ? "white" : "#bbb",
              }}
            >
              {num}
            </Button>
          ))}
        </Box>
      </Box>
    </div>
  );
};

export default MaxPlayersInput;
