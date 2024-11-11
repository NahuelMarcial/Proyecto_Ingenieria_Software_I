// Contenedor para la creacion de una partida
import React, { useState } from "react";
import CreateGameButton from "../components/CreateGameButton";
import GameForm from "../components/GameForm";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { handleCreateGame } from "../services/createGameLogic";
import { useNavigate } from "react-router-dom";
import { Box, Typography } from "@mui/material";

const CreateGameContainer = () => {
  const [openForm, setOpenForm] = useState(false);
  const [formData, setFormData] = useState({
    nombre: "",
    owner: "",
    max_jugadores: "",
    password: "",
    dificil: false,
  });
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleButtonClick = () => setOpenForm(true);
  const handleClose = () => setOpenForm(false);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleDifficultyChange = (isDifficult) => {
    setFormData((prevData) => ({
      ...prevData,
      dificil: isDifficult,
    }));
  };

  // Manejar el envio del formulario
  const handleSubmit = (event) => {
    event.preventDefault();
    handleCreateGame(formData, setLoading, handleClose).then((response) => {
      if (response) {
        const partida_id = sessionStorage.getItem("partida_id");
        navigate(`/lobby/${partida_id}`);
      }
    });
  };

  return (
    <div>
      <CreateGameButton onClick={handleButtonClick} />
      <Dialog
        data-testid="create-game-form"
        open={openForm}
        onClose={handleClose}
      >
        <Box
          sx={{
            backgroundColor: "#f0f0f0",
            justifyContent: "center",
            alignContent: "center",
            margin: 1,
          }}
        >
          <DialogTitle
            maxWidth="100%"
            borderBottom={"2px solid #ddd"}
            variant="h1"
            color="secondary"
            sx={{ padding: 1, marginLeft: 2, marginRight: 2, marginTop: 2 }}
          >
            Crear Partida:
          </DialogTitle>
          <DialogContent sx={{ width: "80%", margin: "auto" }}>
            <GameForm
              formData={formData}
              onInputChange={handleInputChange}
              onSubmit={handleSubmit}
              loading={loading}
              onDifficultyChange={handleDifficultyChange}
            />
          </DialogContent>
          <DialogActions data-test="button-cancel-game">
            <Button
              onClick={handleClose}
              variant="outlined"
              color="secondary"
              sx={{
                fontWeight: "bold",
                fontSize: "clamp(0.7rem, 2.5vw, 1.17rem)",
                marginRight: 2,
                marginBottom: 2,
                boxShadow: 0,
                "&:hover": { backgroundColor: "secondary", boxShadow: 2 },
              }}
            >
              Cancelar
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </div>
  );
};

export default CreateGameContainer;
