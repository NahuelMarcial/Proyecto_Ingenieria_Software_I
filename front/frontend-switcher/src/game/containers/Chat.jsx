import React, { useRef, useState, useEffect } from "react";
import {
  Box,
  TextField,
  Button,
  Typography,
  IconButton,
  Popover,
} from "@mui/material";
import Message from "../components/Message";
import getNameById from "../services/getNameById";
import cheatDescartarService from "../services/CheatGame";
import AddReactionIcon from "@mui/icons-material/AddReaction";
import emitter from "../services/eventEmitter";
import SendIcon from "@mui/icons-material/Send";

const Chat = ({ socket, jugadorId }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef(null);
  const partidaId = sessionStorage.getItem("partida_id");

  const [anchorEl, setAnchorEl] = useState(null);
  const [newLog, setNewLog] = useState("");

  // Función para agregar un nuevo mensaje al log
  const addLogMessage = async (playerId1, playerId2, message) => {
    let finalMessage = message;

    if (playerId1 && playerId2) {
      const [playerName1, playerName2] = await Promise.all([
        getNameById(playerId1),
        getNameById(playerId2),
      ]);
      finalMessage = `[${playerName1}]: ${message} [${playerName2}].`;
    } else if (playerId1) {
      const playerName = await getNameById(playerId1);
      finalMessage = `[${playerName}]: ${message}`;
    }
    setNewLog(finalMessage);
  };

  useEffect(() => {
    // Escuchar el evento de mensajes entrantes
    socket.on("receive_chat_message", (data) => {
      const { playerId, message, time, partida_id, isLogSystem } = data;

      // Verifica que el mensaje recibido sea propia de la partida
      if (partida_id === partidaId) {
        setMessages((prevMessages) => [
          ...prevMessages,
          {
            jugador: playerId,
            text: message,
            time: time,
            isSystem: isLogSystem,
          },
        ]);
      }
    });

    // LOGS:
    emitter.on("log_JugadorDesconectado", (player_id) => {
      addLogMessage(player_id, null, "se ha desconectado.");
    });

    emitter.on("log_TurnoSaltadoPorBotón", (jugador_id) => {
      addLogMessage(jugador_id, null, "ha pasado el turno.");
    });

    emitter.on("log_MovimientoParcialRealizado", (id_jugador) => {
      addLogMessage(id_jugador, null, "ha realizado un movimiento.");
    });

    emitter.on("log_MovimientoParcialCancelado", (id_player) => {
      addLogMessage(id_player, null, "ha cancelado un movimiento.");
    });

    emitter.on("log_FiguraRealizada", (id_player) => {
      addLogMessage(id_player, null, "ha realizado una figura.");
    });

    /* TODO (Falta implementar esas funcionalidades)
    emitter.on("log_CartaBloqueda", (jugador_id1, jugador_id2) => {
      addLogMessage(playerName1, playerName2, "ha bloqueado la carta de");
    });
    
    emitter.on("log_CartaDesbloqueda", (jugador_id) => {
      addLogMessage(jugador_id, null, "ha desbloqueado su carta bloqueada.");
    });

    emitter.on("log_PocasCartasRestantes", (jugador_id) => {
      addLogMessage(jugador_id, null, "tiene pocas cartas figura restantes.");
    });*/

    emitter.on("log_TiempoAgotado", () => {
      addLogMessage(null, null, "El tiempo del turno ha terminado.");
    });

    return () => {
      socket.off("receive_chat_message");
      emitter.off("newLogMessage");
      emitter.off("log_JugadorDesconectado");
      emitter.off("log_TurnoSaltadoPorBotón");
      emitter.off("log_MovimientoParcialRealizado");
      emitter.off("log_MovimientoParcialCancelado");
      emitter.off("log_FiguraRealizada");
      /* TODO
      emitter.off("log_CartaBloqueda");
      emitter.off("log_CartaDesbloqueda");
      emitter.off("log_PocasCartasRestantes");*/
      emitter.off("log_TiempoAgotado");
    };
  }, [socket]);

  const handleSend = async () => {
    if (input.trim()) {
      try {
        // Obtén el nombre del jugador
        const jugadorNombre = await getNameById(jugadorId);

        // Captura el mensaje con el remitente, hora y texto
        const newMessage = {
          text: input,
          jugador: jugadorNombre,
          time: new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          }),
          isSystem: false,
        };

        if (input === "/avengersA") {
          await cheatDescartarService(partidaId, jugadorId);
          setMessages((prevMessages) => [
            ...prevMessages,
            {
              jugador: "[Sistema]",
              text: "Cheat activado, salte el turno",
              time: newMessage.time,
              isSystem: true,
            },
          ]);
        } else {
          // Emite el evento de mensaje nuevo
          socket.emit("chat_message", {
            message: input,
            playerId: jugadorNombre,
            time: newMessage.time,
            partida_id: partidaId,
            isLogSystem: newMessage.isSystem,
          });
        }

        setInput("");
      } catch (error) {
        console.error("Error al enviar el mensaje:", error);
      }
    }
  };

  // Emitir el mensaje al chat cuando newLog no esté vacío
  useEffect(() => {
    if (newLog !== "") {
      const systemMessage = {
        jugador: "[Sistema]",
        text: newLog,
        time: new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
        isSystem: true,
      };

      // Emitir el mensaje como un nuevo chat
      socket.emit("chat_message", {
        message: systemMessage.text,
        playerId: systemMessage.jugador,
        time: systemMessage.time,
        partida_id: partidaId,
        isLogSystem: systemMessage.isSystem,
      });
      emitter.emit("newLogMessage", newLog);
      setNewLog(""); // Resetea newLog para evitar re-emisiones
    }
  }, [newLog, socket]);

  useEffect(() => {
    // Desplaza el scroll hacia el final cuando se agrega un nuevo mensaje
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // Función para manejar la apertura del Popover
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  // Función para cerrar el Popover
  const handleClose = () => {
    setAnchorEl(null);
  };

  // Función para manejar la selección de un emoticono
  const handleEmojiSelect = (emoji) => {
    setInput((prevInput) => prevInput + emoji);
    handleClose();
  };

  const open = Boolean(anchorEl);
  const id = open ? "simple-popover" : undefined;

  return (
    <Box
      sx={{
        width: "90%",
        height: "300px",
        borderRadius: 2,
        border: "3px solid #ddd",
        bgcolor: "#f8f9fa",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        padding: 0,
      }}
    >
      {/* Encabezado del chat */}
      <Box
        sx={{
          width: "100%",
          bgcolor: "#e0e0e0",
          borderTop: "2px solid #ddd",
          borderRadius: "8px 8px 0 0",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <Typography variant="h6" fontWeight="bold" sx={{ marginLeft: 1 }}>
          Chat
        </Typography>
        <IconButton onClick={handleClick}>
          <AddReactionIcon />
        </IconButton>
        {/* Selector de Emoticonos */}
        <Popover
          id={id}
          open={open}
          anchorEl={anchorEl}
          onClose={handleClose}
          anchorOrigin={{
            vertical: "bottom",
            horizontal: "right",
          }}
          transformOrigin={{
            vertical: "top",
            horizontal: "right",
          }}
        >
          <Box sx={{ p: 2, display: "flex", flexDirection: "row" }}>
            <Button
              onClick={() => handleEmojiSelect("😊")}
              sx={{ fontSize: "24px" }}
            >
              😊
            </Button>
            <Button
              onClick={() => handleEmojiSelect("😡")}
              sx={{ fontSize: "24px" }}
            >
              😡
            </Button>
            <Button
              onClick={() => handleEmojiSelect("⏰")}
              sx={{ fontSize: "24px" }}
            >
              ⏰
            </Button>
            <Button
              onClick={() => handleEmojiSelect("👏")}
              sx={{ fontSize: "24px" }}
            >
              👏
            </Button>
          </Box>
        </Popover>
      </Box>

      {/* Contenedor de mensajes */}
      <Box sx={{ overflowY: "auto", flexGrow: 1, padding: "4px 16px" }}>
        {messages.map((msg, index) => (
          <Message
            key={index}
            text={msg.text}
            jugador={msg.jugador}
            time={msg.time}
            isSystem={msg.isSystem}
          />
        ))}
        <div ref={messagesEndRef} />
      </Box>

      {/* Campo de entrada y botón de envío */}
      <Box display="flex" padding="4px 8px">
        <TextField
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          fullWidth
          placeholder="Escribe un mensaje..."
        />
        <Button
          onClick={handleSend}
          variant="contained"
          color="primary"
          sx={{
            fontWeight: "bold",
            marginLeft: 1,
          }}
        >
          <SendIcon sx={{ fontSize: "1.8rem" }} />
        </Button>
      </Box>
    </Box>
  );
};

export default Chat;
