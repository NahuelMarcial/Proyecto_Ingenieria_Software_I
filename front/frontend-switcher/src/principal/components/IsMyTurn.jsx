import React from "react";
import { Typography, Box } from "@mui/material";
import { motion } from "framer-motion";

const IsMyTurn = () => {
  return (
    <Box
      component={motion.div}
      sx={{
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        borderRadius: 2,
        border: 3,
        borderColor: "primary.dark",
        padding: 1.1,
        bgcolor: "white",
        minWidth: "clamp(5rem, 5vw, 5rem)",
        minHeight: "clamp(1.8rem, 2.0vw, 2.0rem)",
        maxHeight: "clamp(1.8rem, 2.0vw, 2.0rem)",
      }}
      animate={{
        x: [0, -5, 5, -5, 5, 0], // Movimiento de sacudida
      }}
      transition={{
        duration: 0.5, // Duración de la animación
        repeat: Infinity, // Repetición infinita
        repeatType: "loop",
        repeatDelay: 2, // Lapso de tiempo en segundos antes de que la animación se repita
      }}
    >
      <Typography variant="h4" sx={{ fontWeight: 500 }}>
        ¡Tu turno!
      </Typography>
    </Box>
  );
};

export default IsMyTurn;
