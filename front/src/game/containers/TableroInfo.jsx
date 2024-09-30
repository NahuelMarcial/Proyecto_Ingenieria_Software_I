import React, { useState, useEffect } from "react";
import { Box, Button } from "@mui/material";
import PlayersTurn from "../components/PlayersTurn";
import Timer from "../components/Timer";
import ForbiddenColor from "../components/ForbiddenColor";
import Tablero from "../components/Tablero";
import { getCurrentTurn, endTurn } from "../services/turnoService"; // Funciones para la API

const TableroInfo = ({ players, fichas, socket }) => {
  // socket viene como parámetro
  const partida_id = sessionStorage.getItem("partida_id");
  const player_id = sessionStorage.getItem("jugador_id");

  // Temporizador
  const [time, setTime] = useState(120);
  const [timeIsEnding, setTimeIsEnding] = useState(false);

  // Turno de jugador
  const [currentPlayerId, setCurrentPlayerId] = useState("");

  // Color prohibido
  const [forbiddenColor, setForbiddenColor] = useState(1);
  const colors = ["None", "red", "blue", "green", "yellow"];

  // Obtener el turno actual
  useEffect(() => {
    const fetchTurno = async () => {
      const playerId = await getCurrentTurn(partida_id);
      console.log("ID del jugador del turno actual:", playerId);
      setCurrentPlayerId(playerId);
    };

    fetchTurno();
  }, [partida_id]);

  // Escuchar el evento 'turno_pasado' desde el socket
  useEffect(() => {
    // Cuando el socket reciba el evento 'turno_pasado'
    socket.on("turno_pasado", () => {
      console.log("Evento 'turno_pasado' recibido, actualizando turno...");
      // Volver a obtener el turno actual
      const fetchTurno = async () => {
        const playerId = await getCurrentTurn(partida_id);
        setCurrentPlayerId(playerId); // Actualizar el turno en el frontend
      };
      fetchTurno();
    });

    // Limpiar el evento al desmontar el componente
    return () => {
      socket.off("turno_pasado");
    };
  }, [partida_id, socket]);

  useEffect(() => {
    console.log("currentPlayerId:", currentPlayerId);
  }, [currentPlayerId]);

  useEffect(() => {
    // Funcionalidad de temporizador
    const timerInterval = setInterval(() => {
      setTime((prevTime) => {
        const newTime = prevTime > 0 ? prevTime - 1 : 0;

        // Si el tiempo está terminando
        if (newTime <= 120 * 0.1) {
          setTimeIsEnding(true);
        } else {
          setTimeIsEnding(false);
        }

        return newTime;
      });
    }, 1000);

    // Limpiar el intervalo cuando se desmonte el componente
    return () => clearInterval(timerInterval);
  }, []);

  // Manejar la acción de "Saltar Turno"
  const handleSkipTurn = async () => {
    const result = await endTurn(partida_id, player_id);
    if (result) {
      console.log("Turno saltado. Nuevo jugador en turno:", result);
      setCurrentPlayerId(result); // Actualizar el turno al siguiente jugador
      socket.emit("turno_pasado", { partida_id }); // Emitir evento a todos los jugadores
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between",
        alignItems: "flex-start",
        padding: "10px",
        width: "600px",
        height: "300px",
        border: "2px solid black",
        borderRadius: "8px",
        backgroundColor: "#f0f0f0",
      }}
    >
      {/* Caja de información del turno */}
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          alignItems: "flex-start",
          padding: "10px",
          width: "30%",
          borderRadius: "8px",
          backgroundColor: "#f0f0f0",
        }}
      >
        <PlayersTurn PlayerName={currentPlayerId} />
        <Timer Time={time} TimeIsEnding={timeIsEnding} />
        <ForbiddenColor Color={colors[forbiddenColor]} />
        <Button
          variant="contained"
          sx={{
            backgroundColor: "red",
            color: "white",
            marginTop: "16px",
            width: "100%",
            height: "56px",
            borderRadius: "8px",
          }}
          onClick={handleSkipTurn}
          disabled={currentPlayerId !== player_id} // Desactiva si no es el turno del jugador
        >
          Saltar Turno
        </Button>
      </Box>

      {/* Caja con tablero */}
      <Box
        sx={{
          width: "50%",
          height: "98%",
          paddingLeft: "10px",
        }}
      >
        <Tablero fichas={fichas} />
      </Box>
    </Box>
  );
};

export default TableroInfo;
