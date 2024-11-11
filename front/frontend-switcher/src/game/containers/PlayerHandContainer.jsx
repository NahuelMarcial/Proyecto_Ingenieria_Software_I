import PlayerHand from "../components/PlayerHand";
import { useEffect, useState } from "react";
import getFigCardsPlayer from "../services/getFigCardsPlayer";
import getMovCardsPlayer from "../services/getMovCardsPlayer";
import figureImages from "../services/figureImages";
import movImages from "../services/movImages";
import { getCurrentTurn } from "../services/turnoService"; // Funciones para la API
import emitter from "../services/eventEmitter";
import { useNavigate } from "react-router-dom";

const PlayerHandContainer = ({ jugador, socket, width, height }) => {
  const [figureCards, setFigureCards] = useState([]);
  const [movCards, setMovCards] = useState([]);
  const [currentTurn, setCurrentTurn] = useState(""); // Turno de jugador
  const partida_id = sessionStorage.getItem("partida_id");
  const jugador_id = jugador;
  const navigate = useNavigate();
  // Determinar si el jugador es el host
  const isHost = () => {
    const storedHostId = sessionStorage.getItem("jugador_id");
    return storedHostId === jugador_id;
  };

  // Determinar si es el turno actual
  const fetchTurno = async () => {
    const playerId = await getCurrentTurn(partida_id);
    setCurrentTurn(playerId);
  };

  // Obtener las cartas de figura del jugador
  const auxFigCards = async () => {
    await getFigCardsPlayer(partida_id, jugador_id).then((cards) => {
      const formattedCards = cards.map((card) => ({
        imageSrc: figureImages[card.id_carta], // diccionario para obtener la imagen
        id_carta: card.id_carta,
        id_player: card.id_player,
        title: card.nombre,
        bloqueada: card.bloqueada,
      }));
      setFigureCards(formattedCards);
    });
  };
  // Obtener las cartas de movimiento del jugador
  const auxMovCards = async () => {
    await getMovCardsPlayer(partida_id, jugador_id).then((cards) => {
      const formattedMovCards = cards.map((card) => ({
        imageSrc: movImages[card.id_carta], // diccionario de imágenes de movimientos
        id_carta: card.id_carta,
        title: card.tipo_movimiento,
        gastada: card.gastada,
      }));
      setMovCards(formattedMovCards);
    });
  };

  useEffect(() => {
    if (!jugador) return;

    const fetchData = async () => {
      await auxFigCards();
      await auxMovCards();
      await fetchTurno();
    };

    fetchData();

    const handleSetCartasFiguraCreado = async () => {
      await auxFigCards();
      emitter.emit("set_cartas_figura_creado");
    };

    const handleSetCartasMovimientoCreado = async () => {
      await auxMovCards();
      emitter.emit("set_cartas_movimiento_creado");
    };

    const handleMovimientoRealizado = async () => {
      await auxMovCards();
      emitter.emit("movimiento_realizado");
    };

    const handleCartaFiguraJugada = async () => {
      await auxMovCards();
      await auxFigCards();
      emitter.emit("carta_figura_jugada");
    };

    const handleTurnoPasado = async () => {
      console.log("turno pasado se escucha");
      await auxMovCards();
      await auxFigCards();
      await fetchTurno();
      emitter.emit("turno_pasado_emitter");
    };

    const handleDeshizoMovimiento = async () => {
      await auxMovCards();
      emitter.emit("deshizo_movimiento");
    };

    socket.on("set_cartas_figura_creado", handleSetCartasFiguraCreado);
    socket.on("set_cartas_movimiento_creado", handleSetCartasMovimientoCreado);
    socket.on("movimiento_realizado", handleMovimientoRealizado);
    socket.on("carta_figura_jugada", handleCartaFiguraJugada);
    socket.on("turno_pasado", handleTurnoPasado);
    socket.on("deshizo_movimiento", handleDeshizoMovimiento);

    return () => {
      socket.off("set_cartas_figura_creado", handleSetCartasFiguraCreado);
      socket.off(
        "set_cartas_movimiento_creado",
        handleSetCartasMovimientoCreado
      );
      socket.off("movimiento_realizado", handleMovimientoRealizado);
      socket.off("carta_figura_jugada", handleCartaFiguraJugada);
      socket.off("turno_pasado", handleTurnoPasado);
      socket.off("deshizo_movimiento", handleDeshizoMovimiento);
    };
  }, [jugador]);

  return (
    <PlayerHand
      jugador_id={jugador_id}
      isHost={isHost()}
      figureCards={figureCards}
      movCards={movCards}
      isTurn={currentTurn === jugador_id}
      width={width}
      height={height}
      socket={socket}
    />
  );
};

export default PlayerHandContainer;
