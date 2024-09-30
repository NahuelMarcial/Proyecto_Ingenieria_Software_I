import React from "react";
import { Box } from "@mui/material";

const Ficha = ({ pos_x, pos_y, color }) => {
  return (
    <Box
      sx={{
        backgroundColor: color,
        gridColumn: pos_x,
        gridRow: pos_y,
        borderRadius: "5%",
        border: "1px solid black",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        width: "100%", // Asegúrate de ocupar toda la celda del grid
        height: "100%", // Asegúrate de ocupar toda la celda del grid
        color: "white",
        fontWeight: "bold",
        fontSize: "18px",
      }}
    ></Box>
  );
};

export default Ficha;
