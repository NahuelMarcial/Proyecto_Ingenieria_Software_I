import React, { useState } from "react";
import { Drawer, Button, Box } from "@mui/material";
import GameEntryActiveList from "../../principal/containers/GameEntryActiveList"; // Asegúrate de que la ruta sea correcta

const SideMenu = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDrawer = (open) => (event) => {
    if (
      event.type === "keydown" &&
      (event.key === "Tab" || event.key === "Shift")
    ) {
      return;
    }
    setIsOpen(open);
  };

  return (
    <Box>
      <Button
        sx={{
          width: "100%", // Cambiado para coincidir con los otros botones
          height: "100%",
          backgroundColor: "primary.main",
          color: "white",
          border: 1,
          borderColor: "primary.dark",
          fontSize: "clamp(0.6rem, 1.5vw, 1.5rem)",
          fontWeight: "bold",
          "&:hover": {
            backgroundColor: "primary.light",
          },
          opacity: 1,
        }}
        variant="contained"
        onClick={toggleDrawer(true)}
      >
        Mis Partidas
      </Button>
      <Drawer anchor="left" open={isOpen} onClose={toggleDrawer(false)}>
        <Box
          padding={1}
          role="presentation"
          onClick={toggleDrawer(false)}
          onKeyDown={toggleDrawer(false)}
        >
          <GameEntryActiveList />
        </Box>
      </Drawer>
    </Box>
  );
};

export default SideMenu;
