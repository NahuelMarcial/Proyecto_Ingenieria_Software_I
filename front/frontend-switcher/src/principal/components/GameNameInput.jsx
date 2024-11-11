import React, { useState, useEffect } from "react";
import { TextField, Typography, Box, IconButton } from "@mui/material";
import TagIcon from "@mui/icons-material/LocalOffer";

const GameNameInput = ({ value, onChange }) => {
  const [isNameSet, setIsNameSet] = useState(false);

  const handleChange = (e) => {
    const { value, name } = e.target;

    // Validación de caracteres alfanuméricos y espacios
    const regex = /^[A-Za-z0-9 ]{0,30}$/;

    // Validar el nombre de la partida
    if (regex.test(value) || value === "") {
      onChange({ target: { name, value } });
    }
  };

  useEffect(() => {
    setIsNameSet(value.length > 0);
  }, [value]);

  return (
    <div>
      <Typography
        data-testid="title-name-game-form"
        variant="body2"
        color="text.secondary"
        sx={{
          ml: 1,
          fontSize: { xs: "0.7rem", sm: "0.9rem" }, 
        }}
      >
        Nombre de la Partida *
      </Typography>
      <Box
        padding={1}
        gap={2}
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
            borderColor: isNameSet ? "primary.main" : "#bbb",
            borderRadius: 1,
          }}
        >
          <IconButton disabled={true}>
            <TagIcon
              fontSize="large"
              sx={{ 
                color: isNameSet ? "primary.main" : "#bbb",
                fontSize: { xs: "1.7rem", sm: "2.3rem" }, 
              }}
            />
          </IconButton>
        </Box>
        <TextField
          fullWidth
          name="nombre"
          placeholder="Intoducir nombre..."
          variant="outlined"
          color="secondary"
          value={value}
          onChange={handleChange}
          required
        />
      </Box>
    </div>
  );
};

export default GameNameInput;
