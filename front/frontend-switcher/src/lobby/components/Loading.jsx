import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import colors from "../../configs/colors";
import { Box, Typography } from "@mui/material";


// Crear MotionBox a partir de Box
const MotionBox = motion.create(Box);

const Loading = () => {
  const colorKeys = Object.keys(colors).filter((color) => color !== "gris");

  const [zIndex1, setZIndex1] = useState(2);
  const [zIndex2, setZIndex2] = useState(1);
  const [colorIndex1, setColorIndex1] = useState(0);
  const [colorIndex2, setColorIndex2] = useState(1);
  const [color1, setColor1] = useState(colors[colorKeys[0]]);
  const [color2, setColor2] = useState(colors[colorKeys[1]]);

  useEffect(() => {
    const interval = setInterval(() => {
      setZIndex1((prev) => (prev === 1 ? 2 : 1));
      setZIndex2((prev) => (prev === 1 ? 2 : 1));
      setColorIndex1((prevIndex) => (prevIndex + 1) % colorKeys.length);
      setColorIndex2((prevIndex) => (prevIndex + 1) % colorKeys.length);
    }, 2050);

    return () => {
      clearInterval(interval);
    };
  }, [colorKeys.length]);

  useEffect(() => {
    setColor1(colors[colorKeys[colorIndex1]]);
    setColor2(colors[colorKeys[colorIndex2]]);
  }, [colorIndex1, colorIndex2, colorKeys]);

  return (
    <Box
      sx={{ 
        width: "10%",
        height: "10%",
        position: "fixed", 
        bottom: { xs: 80, sm: 100 }, 
        right: { xs: "16vw", sm: "6vw", md: "4vw" }, 
        zIndex: 999,
      }}
    >
      <Typography variant="h3" fontSize="1rem" marginBottom={0} >
        Esperando
      </Typography>
      <Typography variant="h3" fontSize="1rem" marginBottom={3} >
        jugadores
      </Typography>
      <MotionBox
        className="box1"
        animate={{
          scale: [1, 1.5, 1, 1],
          x: [16, 56, 16],
          y: [-10, 30, -10],
        }}
        transition={{
          duration: 4.1,
          ease: "easeInOut",
          repeat: Infinity,
          repeatType: "loop",
          delay: 0,
        }}
        style={{
          position: "absolute",
          zIndex: zIndex1,
          background: color1,
          borderRadius: 5,
          border: `2px solid black`,
        }}
        sx={{
          width: { xs: 20, sm: 25 },
          height: { xs: 20, sm: 25 },
        }}
      />
      <MotionBox
        className="box2"
        animate={{
          scale: [1, 1, 1.5, 1],
          x: [56, 16, 56],
          y: [30, -10, 30],
        }}
        transition={{
          duration: 4.1,
          ease: "easeInOut",
          repeat: Infinity,
          repeatType: "loop",
          delay: 0,
        }}
        style={{
          position: "absolute",
          zIndex: zIndex2,
          background: color2,
          borderRadius: 5,
          border: `2px solid black`,
        }}
        sx={{
          width: { xs: 20, sm: 25 },
          height: { xs: 20, sm: 25 },
        }}
      />
    </Box>
  );
};

export default Loading;
