import { Button } from "@mui/material";

const SaltarTurno = ({ handleSkipTurn, isTurn }) => {
  return (
    <Button
      variant="contained"
      sx={{
        width: 136,
        height: 35,
        backgroundColor: "error.main",
        color: "white",
        border: 1,
        fontSize: 14,
        fontWeight: "bold",
        "&:hover": {
          backgroundColor: "error.light",
        },
      }}
      onClick={handleSkipTurn}
      disabled={!isTurn} // Desactiva si no es el turno del jugador
    >
      Pasar Turno
    </Button>
  );
};

export default SaltarTurno;
