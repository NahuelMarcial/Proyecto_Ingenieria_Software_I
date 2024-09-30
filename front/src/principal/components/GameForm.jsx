import React from "react";
import { TextField, Button, Box } from "@mui/material";

const GameForm = ({ formData, onInputChange, onSubmit, loading }) => {
  // Manejar el cambio de los inputs del formulario
  const handleChange = (e) => {
    const { name, value } = e.target;

    // Validación de caracteres alfanuméricos y espacios
    const regex = /^[A-Za-z0-9 ]{0,30}$/;

    // Validar el nombre de la partida
    if (name === "nombre") {
      if (regex.test(value) || value === "") {
        onInputChange(e);
      }
    } else {
      onInputChange(e);
    }
  };

  return (
    <Box
      component="form"
      onSubmit={onSubmit}
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 3, // Usando el sistema de espaciado del tema (multiplo de 8px)
        width: "100%",
        maxWidth: "500px",
        margin: "0 auto",
        marginTop: 2, // Espaciado según el tema
      }}
    >
      <TextField
        name="nombre"
        label="Nombre de la Partida"
        variant="outlined"
        color="secondary" // Usando el color secundario del tema
        value={formData.nombre}
        onChange={handleChange}
        required
      />
      <TextField
        name="max_jugadores"
        label="Máximo de Jugadores"
        variant="outlined"
        color="secondary" // Usando el color secundario del tema
        type="number"
        inputProps={{ min: 2, max: 4 }}
        value={formData.max_jugadores}
        onChange={onInputChange}
        required
      />
      <Button
        type="submit"
        variant="contained"
        color="primary" // Usando el color primario del tema
        disabled={loading}
        sx={{ "&:hover": { backgroundColor: "primary.light" } }}
      >
        {loading ? "Creando..." : "Crear"}
      </Button>
    </Box>
  );
};

export default GameForm;
