import React, { useEffect, useState } from "react";
import { Button, Box } from "@mui/material";
import PasswordInput from "./PasswordInput";
import MaxPlayersInput from "./MaxPlayersInput";
import GameNameInput from "./GameNameInput";
import SwitchDifficulty from "./SwitchDifficulty";

const GameForm = ({
  formData,
  onInputChange,
  onSubmit,
  loading,
  onDifficultyChange,
}) => {
  const [isPrivate, setIsPrivate] = useState(false);
  const [actualPassword, setActualPassword] = useState("");
  const [isAvailableToSend, setIsAvailableToSend] = useState(false);

  // Maneja el cambio de la contraseña
  const handlePasswordChange = (password) => {
    onInputChange({ target: { name: "password", value: password } });
    setActualPassword(password);
    if (password.length === 0) {
      setIsPrivate(false);
    } else {
      setIsPrivate(true);
    }
  };

  // Validación de los campos
  const [errors, setErrors] = useState({
    nombre: true,
    max_jugadores: true,
    password: false,
  });

  useEffect(() => {
    const nombreError = formData.nombre.length === 0;
    const maxJugadoresError =
      formData.max_jugadores < 2 || formData.max_jugadores > 4;
    const passwordError = isPrivate && formData.password.length !== 4;

    setErrors({
      nombre: nombreError,
      max_jugadores: maxJugadoresError,
      password: passwordError,
    });

    setIsAvailableToSend(!nombreError && !maxJugadoresError && !passwordError);
  }, [formData, actualPassword]);

  return (
    <Box
      component="form"
      onSubmit={onSubmit}
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 1,
        width: "100%",
        maxWidth: "500px",
        margin: "0 auto",
        marginTop: 2,
      }}
    >
      <GameNameInput value={formData.nombre} onChange={onInputChange} />
      <MaxPlayersInput
        value={formData.max_jugadores}
        onChange={onInputChange}
      />
      <PasswordInput setPassword={handlePasswordChange} isPrivate={isPrivate} />
      <SwitchDifficulty onChange={onDifficultyChange} />
      <Button
        type="submit"
        variant="contained"
        color="primary"
        disabled={loading || !isAvailableToSend}
        sx={{
          boxShadow: 0,
          fontSize: "clamp(0.7rem, 2.5vw, 1.17rem)",
          fontWeight: "bold",
          "&:hover": { backgroundColor: "primary", boxShadow: 2 },
        }}
      >
        {loading ? "Creando..." : "Crear"}
      </Button>
    </Box>
  );
};

export default GameForm;
