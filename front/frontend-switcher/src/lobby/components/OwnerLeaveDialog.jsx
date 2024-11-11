import React from "react";
import { Dialog, DialogTitle, DialogActions, Button } from "@mui/material";
import { styled } from "@mui/system";
import PersonOffIcon from "@mui/icons-material/PersonOff";

const StyledDialog = styled(Dialog)(({ theme }) => ({
  "& .MuiDialogTitle-root": {
    backgroundColor: "#ff4d4d", // Fondo verde
    color: "white",
    fontSize: "24px",
    textAlign: "center",
    padding: theme.spacing(2),
  },
  "& .MuiDialog-paper": {
    padding: theme.spacing(2),
    borderRadius: "8px",
  },
}));

const OwnerLeftDialog = ({ open, onClose }) => {
  return (
    <StyledDialog open={open} onClose={onClose}>
      <DialogTitle sx={{ width: "300px" }}>
        <PersonOffIcon style={{ marginRight: "8px" }} />
        <div>OH NO!!! :(</div>
        <div>El dueño se ha desconectado la partida.</div>
      </DialogTitle>
      <DialogActions>
        <Button
          variant="outlined"
          color="error"
          onClick={onClose}
          style={{ marginTop: "10px" }}
          sx={{ fontSize: 20, margin: "auto", width: "50%" }}
        >
          Salir
        </Button>
      </DialogActions>
    </StyledDialog>
  );
};

export default OwnerLeftDialog;
