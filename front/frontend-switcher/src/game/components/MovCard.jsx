import React from "react";
import { Card, CardActionArea, CardMedia } from "@mui/material";
import { motion } from "framer-motion";

const MovCard = ({ imageSrc, title, isClicked, onClick, gastada }) => {
  return (
    <Card
      sx={{
        width: 110,
        position: "relative",
        padding: "2px",
        borderRadius: "8px",
        border: isClicked && !gastada ? "4px solid orange" : "2px solid grey",
        transform: isClicked && !gastada ? "scale(1.02)" : "scale(1)",
        boxShadow:
          isClicked && !gastada ? "5px 5px 2px rgba(0, 0, 0, 0.4)" : "none",
        transition: "transform 0.3s, border 0.3s",
        opacity: gastada ? 0.5 : 1, // Opacidad baja si la carta está gastada
      }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}  // Transición suave
    >
      <CardActionArea onClick={onClick} disabled={gastada}>
        <CardMedia component="img" height="160" image={imageSrc} alt={title} />
      </CardActionArea>
    </Card>

  );
};

export default MovCard;
