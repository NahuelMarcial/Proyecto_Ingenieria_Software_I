import React, { useState } from "react";
import {
  TextField,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
} from "@mui/material";

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
    >
      <DialogTitle variant="h2" color="primary">
        Bienvendio!
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
