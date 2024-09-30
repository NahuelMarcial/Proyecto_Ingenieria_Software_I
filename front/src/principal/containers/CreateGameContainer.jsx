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
import { Typography } from "@mui/material";

const CreateGameContainer = () => {
  const [openForm, setOpenForm] = useState(false); // estado para abrir/cerrar el formulario
  const [formData, setFormData] = useState({
    // estado para los datos del formulario
    nombre: "",
    owner: "",
    max_jugadores: "",
  });
  const [loading, setLoading] = useState(false); // estado para el boton de carga
  const navigate = useNavigate(); // hook para navegar entre rutas

  const handleButtonClick = () => setOpenForm(true); // abrir el formulario al hacer click
  const handleClose = () => setOpenForm(false); // cerrar el formulario

  // manejar el cambio de los inputs del formulario
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // manejar el envio del formulario
  const handleSubmit = (event) => {
    event.preventDefault();
    handleCreateGame(formData, setLoading, handleClose).then(() => {
      // obtener partida_id de sessionStorage
      const partida_id = sessionStorage.getItem("partida_id");
      // navegar al lobby usando partida_id
      navigate(`/lobby/${partida_id}`);
    });
  };

  return (
    <div>
      <CreateGameButton onClick={handleButtonClick} />
      <Dialog open={openForm} onClose={handleClose}>
        <DialogTitle
          width={450}
          borderBottom={"1px solid #ddd"}
          margin={"0 auto"}
        >
          <Typography
            fontSize="21px"
            fontWeight="bold"
            color="secondary"
            sx={{ marginTop: 2 }}
          >
            Crear Partida
          </Typography>
        </DialogTitle>
        <DialogContent sx={{ width: "500px" }}>
          <GameForm
            formData={formData}
            onInputChange={handleInputChange}
            onSubmit={handleSubmit}
            loading={loading}
          />
        </DialogContent>
        <DialogActions>
          <Button
            onClick={handleClose}
            variant="outlined"
            color="secondary"
            sx={{ fontWeight: "bold", marginRight: 2, marginBottom: 2 }}
          >
            Cancelar
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default CreateGameContainer;
