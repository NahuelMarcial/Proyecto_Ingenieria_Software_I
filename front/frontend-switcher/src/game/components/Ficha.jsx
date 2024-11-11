import React, { useEffect, useState } from "react";
import { Button } from "@mui/material";
import { motion } from "framer-motion";
import { lighten } from "@mui/system";
import emitter from "../services/eventEmitter";
import getDifficult from "../services/getDifficult";

const Ficha = ({ id_ficha, pos_x, pos_y, color, inFig, inSugerencia }) => {
  const [disabled, setDisabled] = useState(true);
  const [selectedCardType, setSelectedCardType] = useState(null);
  const [isPossibleMove, setIsPossibleMove] = useState(false);
  const [isClicked, setIsClicked] = useState(false);
  const [opacity, setOpacity] = useState(1);
  const [resetAnimation, setResetAnimation] = useState(false);
  const [isDifficult, setIsDifficult] = useState(false);

  const handleClick = () => {
    if (selectedCardType === "mov") {
      setIsClicked(true);
    }

    if (!disabled) {
      if (selectedCardType === "mov") {
        emitter.emit("tileSelectedAfterMov", id_ficha);
        console.log("Se seleccionó una ficha después de movimiento:", id_ficha);
      } else if (selectedCardType === "fig") {
        emitter.emit("tileSelectedAfterFig", id_ficha);
        console.log("Se seleccionó una ficha después de figura:", id_ficha);
      }
    }
  };

  useEffect(() => {
    getDifficult().then((difficult) => {
      setIsDifficult(difficult);
      console.log("Dificultad:", difficult);
    });

    const handleMovCardClick = (isClicked) => {
      setDisabled(!isClicked);
      setSelectedCardType("mov");
      if (!isClicked) {
        setIsPossibleMove(false);
        setIsClicked(false);
        setOpacity(1);
      }
    };

    const handleFigCardClick = (isClicked) => {
      setDisabled(!isClicked);
      setSelectedCardType("fig");
    };

    const handleFirstTileSelected = (possibleTiles) => {
      const isPossibleMove = possibleTiles.some(
        (tile) => tile.id_ficha === id_ficha
      );
      setIsPossibleMove(isPossibleMove);
      setDisabled(!isPossibleMove);
      setOpacity(isPossibleMove ? 1 : 0.7);
    };

    const handleMovCompleted = () => {
      setIsPossibleMove(false);
      setIsClicked(false);
      setOpacity(1);
      setResetAnimation(true);
    };

    emitter.on("movCardClicked", handleMovCardClick);
    emitter.on("figCardClicked", handleFigCardClick);
    emitter.on("firstTileSelected", handleFirstTileSelected);
    emitter.on("movCompleted", handleMovCompleted);
    emitter.on("movCardSelected", handleMovCompleted);
    emitter.on("turno_pasado_emitter", handleMovCompleted);
    emitter.on("CancelMovement", handleMovCompleted);

    return () => {
      emitter.off("movCardClicked", handleMovCardClick);
      emitter.off("figCardClicked", handleFigCardClick);
      emitter.off("firstTileSelected", handleFirstTileSelected);
      emitter.off("movCompleted", handleMovCompleted);
      emitter.off("movCardSelected", handleMovCompleted);
      emitter.off("turno_pasado_emitter", handleMovCompleted);
      emitter.off("CancelMovement", handleMovCompleted);
    };
  }, []);

  useEffect(() => {
    // reinicia la animación despues que el componente se renderice
    if (resetAnimation) {
      const timeout = setTimeout(() => {
        setResetAnimation(false);
      }, 150);

      return () => clearTimeout(timeout);
    }
  }, [resetAnimation]);

  return (
    <Button
      disabled={disabled}
      component={inFig ? motion.div : "div"}
      data-testid={`ficha-${pos_x}-${pos_y}`}
      sx={{
        backgroundColor: color,
        gridColumn: pos_x,
        gridRow: pos_y,
        borderRadius: "7px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        width: 60,
        height: 60,
        border: isClicked
          ? "4px solid orange"
          : inSugerencia
          ? "4px solid purple" && !isDifficult
          : isPossibleMove && !isDifficult
          ? "4px solid white"
          : `3px solid ${inFig ? lighten(color, 0.55) : "black"}`,
        opacity: isClicked ? 1 : opacity,
        "&:hover": {
          border: "4px solid orange",
          transition: "border 0.1s ease-in-out",
        },
      }}
      animate={
        inFig && !resetAnimation
          ? {
              scale: [1, 1.06, 1],
              rotate: [0, 5, -5, 0],
              backgroundColor: [color, lighten(color, 0.4), color],
            }
          : {}
      }
      transition={
        inFig && !resetAnimation
          ? {
              duration: 0.5,
              ease: "easeInOut",
              repeat: Infinity,
              repeatDelay: 0.7,
            }
          : {}
      }
      onClick={handleClick}
    >
      {id_ficha}
    </Button>
  );
};

export default Ficha;
