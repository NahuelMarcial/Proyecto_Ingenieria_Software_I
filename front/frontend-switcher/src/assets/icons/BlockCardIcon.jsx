import React from "react";
import { Box } from "@mui/material";
import CandadoIcon from "./CandadoIcon";
import Chain from "./ChainIcon";

const BlockCardIcon = ({ size = 80 }) => {
  const lockSize = size;
  const chainSize = size * 2.5;

  return (
    <Box
      position="relative"
      display="inline-block"
      width={chainSize}
      height={chainSize}
    >
      {/* Caja con el candado */}
      <Box
        position="absolute"
        top="28%"
        left="28%"
        bgcolor="#e8e8e8"
        border="3px solid"
        borderColor="error.main"
        borderRadius="15%"
        display="flex"
        justifyContent="center"
        alignItems="center"
        zIndex={2}
        sx={{ fontSize: lockSize / 2 }}
      >
        <CandadoIcon
          sx={{
            fontSize: lockSize,
            zIndex: 3,
          }}
        />
      </Box>

      {/* Cadenas */}
      <Chain sx={{ fontSize: chainSize, zIndex: 1 }} />
    </Box>
  );
};

export default BlockCardIcon;
