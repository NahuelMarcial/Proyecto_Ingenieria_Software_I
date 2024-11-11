import React, { useState, useEffect } from "react";
import LockIcon from "@mui/icons-material/Lock";
import PersonIcon from "@mui/icons-material/Person";
import AddIcon from "@mui/icons-material/Add";
import HappyFace from "../../assets/icons/HappyFace";
import AngryFace from "../../assets/icons/AngryFace";

import {
  Box,
  Button,
  Card,
  CardContent,
  DialogContent,
  Typography,
} from "@mui/material";

import joinGameService from "../services/joinGameService";
import { useNavigate } from "react-router-dom";
import PasswordText from "./PasswordText";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";

const GameEntry = ({
  gameName,
  playersCount,
  playersLimit,
  partida_id,
  isPrivate,
  isDifficult,
}) => {
  const navigate = useNavigate(); // hook para navegar entre rutas
  const [openDialog, setOpenDialog] = useState(false);
  const [password, setpassword] = useState("");
  const [error, setError] = useState(false);
  const [invalidPassword, setInvalidPassword] = useState(false);

  const manageHandleJoinClick = () => {
    if (!isPrivate) {
      handleJoinClick();
    } else {
      setOpenDialog(true);
    }
  };
  const handleJoinClick = async () => {
    try {
      // llamar al servicio para unirse a la partida
      const result = await joinGameService(partida_id, password);
      sessionStorage.setItem("partida_id", partida_id);
      sessionStorage.setItem("partida_nombre", gameName);
      console.log("Te has unido a la partida:", result);

      if (result) {
        navigate(`/lobby/${partida_id}`);
      }
      setOpenDialog(false);
    } catch (error) {
      console.error("Error al unirse a la partida:", error);
      setInvalidPassword(true);
    }
  };

  useEffect(() => {
    setError(isPrivate && password.length !== 0 && password.length !== 4);
  }, [isPrivate, password]);

  const CancelJoin = () => {
    setOpenDialog(false);
    setpassword("");
  };
  return (
    <Card
      variant="outlined"
      sx={{
        position: "relative",
        marginBottom: 0, // Ajuste de espaciado según el theme
        backgroundColor: "primary.main", // Usar color primario desde el tema
        height: { xs: "30px", sm: "40px", md: "44px" },
        transition: "transform 0.3s, box-shadow 0.3s",
        boxShadow: 1, // Usar el primer nivel de sombras del tema
        "&:hover": {
          transform: "translateY(-5px)",
          boxShadow: 2, // Usar el segundo nivel de sombras del tema
        },
      }}
    >
      <CardContent
        sx={{
          padding: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
          sx={{ width: "100%" }}
        >
          <Box display="flex" gap={1}>
            <Typography variant="h3" component="div">
              {gameName}
            </Typography>
          </Box>
          <Box
            display="flex"
            flexDirection="row"
            alignItems="center"
            justifyContent="flex-end"
            gap={1}
          >
            <Box
              sx={{
                display: "inline-flex",
                alignItems: "center",
                justifyContent: "center",
                borderRadius: 2,
                bgcolor: "grey.100",
                border: 3,
                padding: 1,
                width: { xs: "5%", sm: "5%", md: "10%" },
                minWidth: "clamp(1.8rem, 2.0vw, 2.0rem)",
                maxHeight: "clamp(1.8rem, 2.0vw, 2.0rem)",
              }}
            >
              {isDifficult ? (
                <AngryFace sx={{ fontSize: "2rem" }} />
              ) : (
                <HappyFace sx={{ fontSize: "2rem" }} />
              )}
            </Box>

            {isPrivate && (
              <Box
                sx={{
                  display: "inline-flex",
                  alignItems: "center",
                  justifyContent: "center",
                  borderRadius: 2,
                  bgcolor: "grey.100",
                  border: 3,
                  padding: 1,
                  width: { xs: "5%", sm: "5%", md: "10%" },
                  minWidth: "clamp(1.8rem, 2.0vw, 2.0rem)",
                  maxHeight: "clamp(1.8rem, 2.0vw, 2.0rem)",
                }}
              >
                <LockIcon
                  data-testid="lockicon"
                  sx={{ fontSize: { xs: 20, sm: 28, md: 36 } }}
                />
              </Box>
            )}
            <Box
              sx={{
                display: "inline-flex",
                alignItems: "center",
                justifyContent: "center",
                borderRadius: 2,
                bgcolor: "grey.100",
                border: 3,
                padding: 1,
                width: { xs: "5%", sm: "5%", md: "10%" },
                minWidth: "clamp(1.5rem, 3.5vw, 3.5rem)",
                maxHeight: "clamp(1.8rem, 2.0vw, 2.0rem)",
              }}
            >
              <PersonIcon data-testid="personicon" sx={{ fontSize: "2rem" }} />
              <Typography
                variant="body1"
                sx={{
                  fontSize: "1.2rem",
                  fontWeight: "bold",
                }}
              >
                {playersCount}/{playersLimit}
              </Typography>
            </Box>
            <Button
              variant="contained"
              color="secondary" // Usar color secundario desde el tema
              onClick={manageHandleJoinClick}
              sx={{
                fontWeight: "bold",
                padding: { xs: "6px 12px", sm: "8px 16px" },
                fontSize: { xs: "0.75rem", sm: "1rem", md: "1.1rem" },
              }}
            >
              <AddIcon sx={{ fontSize: "2.2rem" }} />
            </Button>
          </Box>
          <Dialog
            open={openDialog}
            data-testid="Dialogpassword"
            onClose={(event, reason) => {
              if (reason !== "backdropClick" && password.trim() !== "") {
                handleJoinClick();
              }
            }}
          >
            <DialogTitle> Ingrese la contraseña</DialogTitle>
            <DialogContent>
              <Box
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  gap: 1,
                  padding: 1,
                }}
              >
                <PasswordText
                  password={password}
                  setPassword={setpassword}
                  error={error || invalidPassword}
                  data-testid="input-pass"
                />
                <Button
                  data-testid="send-pass"
                  variant="contained"
                  color="secondary" // Usar color secundario desde el tema
                  onClick={handleJoinClick}
                  sx={{ fontWeight: "bold" }}
                >
                  Unirse
                </Button>
                <Button
                  variant="contained"
                  color="error" // Usar color secundario desde el tema
                  onClick={CancelJoin}
                  sx={{ fontWeight: "bold" }}
                >
                  Cancelar
                </Button>
                {invalidPassword && (
                  <Typography>La contraseña es incorrecta</Typography>
                )}
              </Box>
            </DialogContent>
          </Dialog>
        </Box>
      </CardContent>
    </Card>
  );
};

export default GameEntry;
