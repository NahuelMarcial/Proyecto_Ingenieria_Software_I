// src/components/TableroInfo.js
import React, { useState, useEffect } from "react";
import { Box } from "@mui/material";
import Timer from "../components/Timer";
import ForbiddenColor from "../components/ForbiddenColor";
import Tablero from "./Tablero";
import colors from "../../configs/colors";
import getColorProhibido from "../services/getColorProhibido";
import { useHandleTime } from "../services/handleTime";

const TableroInfo = ({ socket }) => {
  const { time, timeIsEnding } = useHandleTime(socket);

  // Color prohibido
  const [forbiddenColor, setForbiddenColor] = useState("gris");

  const updateForbiddenColor = async () => {
    const response = await getColorProhibido();
    setForbiddenColor(response.color || "gris");
  };

  useEffect(() => {
    updateForbiddenColor();
    socket.on("carta_figura_jugada", () => {
      updateForbiddenColor();
    });
  }, []);

  return (
    <Box
      display="flex"
      alignItems="center"
      sx={{
        backgroundColor: "white",
        borderRadius: "10px",
        border: "4px solid #ddd",
        padding: "5px",
      }}
    >
      {/* Caja con ForbiddenColor */}
      <Box sx={{ marginRight: "20px", marginLeft: "15px" }}>
        <ForbiddenColor color={colors[forbiddenColor]} />
      </Box>
      {/* Caja con Tablero */}
      <Box>
        <Tablero socket={socket} />
      </Box>
      {/* Caja con Timer */}
      <Box sx={{ marginLeft: "20px", marginRight: "15px" }}>
        <Timer Time={time} TimeIsEnding={timeIsEnding} />
      </Box>
    </Box>
  );
};

export default TableroInfo;
