// src/components/Message.js
import React from "react";
import { Box, Typography } from "@mui/material";

const Message = ({ text, jugador, time, isSystem }) => {
  return (
    <Box display="flex" flexDirection="column">
      <Typography
        variant="caption"
        color="textSecondary"
        sx={{
          fontWeight: "bold",
        }}
      >
        {jugador} - {time}
      </Typography>
      <Typography
        align="right"
        sx={{
          backgroundColor: isSystem ? "secondary.dark" : "#e0e0e0",
          borderRadius: 2,
          padding: "5px 10px",
          maxWidth: "100%",
          wordWrap: "break-word",
          fontSize: isSystem ? "14px" : "20px", // Texto más pequeño si es un mensaje del sistema
          color: isSystem ? "#ffffff" : "inherit",
        }}
      >
        {text}
      </Typography>
    </Box>
  );
};

export default Message;
