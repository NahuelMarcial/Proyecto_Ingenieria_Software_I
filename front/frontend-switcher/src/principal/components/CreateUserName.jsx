import React, { useState } from "react";
import {
  TextField,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
} from "@mui/material";
import createName from "../services/createName";

const SetNickname = () => {
  const [nick, setNick] = useState("");
  const [openForm, setOpenForm] = useState(
    sessionStorage.getItem("jugador_nombre") == null
  );

  const onHandelChange = (event) => {
    setNick(event.target.value);
  };

  const handleClose = () => {
    if (nick.trim() !== null) {
      sessionStorage.setItem("jugador_nombre", nick);
      createName(nick);
      setOpenForm(false);
    } else {
      return;
    }
  };

  return (
    <Dialog
      open={openForm}
      onClose={(event, reason) => {
        if (reason !== "backdropClick" && nick.trim() !== "") {
          handleClose();
        }
      }}
      disableEscapeKeyDown={false}
      sx={{
        "& .MuiDialog-paper": {
          minWidth: { xs: "5%", sm: "10%", md: "30%", lg: "30%"}, // Ancho mínimo en diferentes tamaños de pantalla
          maxWidth: "70%",                              
          minHeight: "280px",                          
          maxHeight: "300px",                            
          padding: 1,
        },
      }}
    >
      <DialogTitle variant="h2" color="primary">
        Bienvenido!
      </DialogTitle>
      <DialogTitle variant="h3" color="secondary">
        Ingrese su nombre de jugador
      </DialogTitle>
      <DialogContent>
        <TextField
          label="nickname"
          value={nick}
          onChange={onHandelChange}
          color="secondary"
          margin="dense"
          sx={{ width: "90%", marginLeft: "5%" }}
        />
        <Button
          onClick={handleClose}
          disabled={nick.trim() === ""}
          variant="outlined"
          color="primary"
          sx={{
            width: "90%",
            marginLeft: "5%",
            marginTop: 2,
            fontWeight: "bold",
          }}
        >
          Guardar
        </Button>
      </DialogContent>
    </Dialog>
  );
};

export default SetNickname;
