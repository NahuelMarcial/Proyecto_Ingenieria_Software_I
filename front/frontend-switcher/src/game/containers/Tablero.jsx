import React, { useState, useEffect } from "react";
import Ficha from "../components/Ficha";
import { Box } from "@mui/material";
import { motion } from "framer-motion";
import getFichas from "../services/getFichas";
import getMarkedFigs from "../services/getMarkedFigs";
import colors from "../../configs/colors";
import emitter from "../services/eventEmitter";
import { getCurrentTurn } from "../services/turnoService";
import getSugerencias from "../services/getSugerencias";

// Función para mapear los colores en español a inglés
const handleColor = (colorEsp) => {
  return colors[colorEsp] || colorEsp;
};

// Función para verificar si una ficha está dentro de las figuras formadas
const isFichaInFigura = (ficha, figurasFormadas) => {
  return figurasFormadas.some((figura) =>
    figura.fichas.some((conjunto) =>
      conjunto.some(([x, y]) => x === ficha.pos_x && y === ficha.pos_y)
    )
  );
};

const Tablero = ({ socket }) => {
  const partida_id = sessionStorage.getItem("partida_id");
  const jugador_id = sessionStorage.getItem("jugador_id");
  const [fichas, setFichas] = useState([]);
  const [figurasFormadas, setFigurasFormadas] = useState([]);
  const [selectedTiles, setSelectedTiles] = useState([]);
  const [currentTurn, setCurrentTurn] = useState(null);
  const [sugerencias, setSugerencias] = useState([]);

  // Dimenciones del tablero (para animacion)
  const tileWidth = 69; // Ancho de cada ficha
  const tileHeight = 65; // Alto de cada ficha
  const boardWidth = 409; // Ancho total del tablero
  const boardHeight = 385; // Alto total del tablero
  const boardOffsetX = 0; // Ajuste en X
  const boardOffsetY = 0; // Ajuste en Y

  // Función para obtener las fichas de la partida
  const fetchFichas = async () => {
    const fetchedFichas = await getFichas(partida_id);
    setFichas(fetchedFichas);
  };

  // Función para obtener las figuras formadas de la partida
  const fetchFigurasFormadas = async () => {
    const fetchedFiguras = await getMarkedFigs(partida_id);
    setFigurasFormadas(fetchedFiguras);
  };

  const fetchCurrentTurn = async () => {
    const currentTurn = await getCurrentTurn(partida_id);
    setCurrentTurn(currentTurn);
  };

  const fetchSugerencias = async () => {
    const sugerencias = await getSugerencias();
    setSugerencias(sugerencias);
    console.log("Sugerencias en Tablero:", sugerencias);
  };

  const fetchData = async () => {
    await fetchFichas(); // Obtener las fichas
    await fetchFigurasFormadas(); // Obtener las figuras formadas
    await fetchCurrentTurn();
    await fetchSugerencias();
  };

  const isFichaInSugerencia = (fichaId) => {
    return (
      sugerencias &&
      (fichaId === sugerencias.id_ficha1 || fichaId === sugerencias.id_ficha2)
    );
  };

  useEffect(() => {
    fetchData();

    socket.on("set_fichas_creado", () => {
      fetchData();
      setSelectedTiles([]); // Limpiar las fichas seleccionadas al cargar nuevas fichas
    });

    socket.on("movimiento_realizado", () => fetchData());

    socket.on("deshizo_movimiento", () => fetchData());

    socket.on("carta_figura_jugada", () => {
      fetchData();
      setSelectedTiles([]); // Limpiar la selección después de un movimiento
    });

    socket.on("turno_pasado", () => fetchData());

    emitter.on("tileSelectedAfterMov", (fichaId) => {
      setSelectedTiles((prev) => {
        // Verificar si fichaId ya está en prev, si no lo está, agregarlo
        if (!prev.includes(fichaId)) {
          return [...prev, fichaId];
        }
        return prev; // Retornar el anterior si ya está incluido
      });
    });

    return () => {
      socket.off("set_fichas_creado");
      socket.off("movimiento_realizado");
      socket.off("carta_figura_jugada");
      socket.off("deshizo_movimiento");
      socket.off("tileSelectedAfterMov");
      socket.off("turno_pasado");
    };
  }, [partida_id, socket]);

  const getFichaPosition = (pos_x, pos_y) => {
    return {
      x: boardOffsetX + (pos_x - 1) * tileWidth,
      y: boardOffsetY + (6 - pos_y) * tileHeight,
    };
  };

  return (
    <Box
      sx={{
        position: "relative",
        width: `${boardWidth}px`,
        height: `${boardHeight}px`,
        backgroundColor: "black",
        border: "3px solid #ddd",
        borderRadius: "10px",
        padding: "5px",
      }}
    >
      {fichas.map((ficha, index) => {
        const isInFigura = isFichaInFigura(ficha, figurasFormadas);
        const isInSugerencia = isFichaInSugerencia(ficha);
        const newPosition = getFichaPosition(ficha.pos_x, ficha.pos_y);

        // Marcar como en movimiento si las posiciones no coinciden
        const isSelected = selectedTiles.includes(ficha.id_ficha);

        return (
          <motion.div
            key={index}
            initial={{
              x: newPosition.x,
              y: newPosition.y,
            }}
            animate={{
              x: newPosition.x,
              y: newPosition.y,
            }}
            transition={{ duration: 0.3, ease: "easeInOut" }}
            style={{
              position: "absolute",
              width: tileWidth,
              height: tileHeight,
              zIndex: isSelected ? 10 : 1,
            }}
          >
            <Ficha
              key={index}
              id_ficha={ficha.id_ficha}
              pos_x={ficha.pos_x}
              pos_y={ficha.pos_y}
              color={handleColor(ficha.color)}
              inFig={isInFigura}
              inSugerencia={isInSugerencia}
            />
          </motion.div>
        );
      })}
    </Box>
  );
};

export default Tablero;
