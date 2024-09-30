import React, { useEffect, useState } from "react";
import CreateGameContainer from "./CreateGameContainer";
import GameListContainer from "./GameList";
import SetNickname from "../components/CreateUserName";
import { Box, Typography, GlobalStyles } from "@mui/material";

const Principal = ({ socket }) => {
  useEffect(() => {
    let notexist = sessionStorage.getItem("jugador_nombre") === null;
    if (notexist) {
    }
  });

  return (
    <div>
      <GlobalStyles
        styles={{
          html: { margin: 0, padding: 0, height: "100%" },
          body: { margin: 0, padding: 0, height: "100%" },
        }}
      />
      <div>
        <div>
          <Box
            display="flex"
            alignItems="center"
            justifyContent="center"
            bgcolor="#FAFAEB" // Fondo oscuro del tema
            padding={2} // Añade padding interno
            borderRadius={2} // Bordes redondeados
            maxWidth="1000px" // Tamaño máximo de 1000px
            margin="0 auto" // Centra horizontalmente la Box en la página
            marginTop={2} // Añade margen superior
            marginBottom={2} // Añade margen inferior
          >
            <Typography variant="h1" color="primary" sx={{ marginRight: 10 }}>
              BIENVENIDO A "EL SWITCHER ONLINE"
            </Typography>
            <CreateGameContainer />
          </Box>
        </div>
        <div>
          <GameListContainer socket={socket} />
          <SetNickname />
        </div>
      </div>
    </div>
  );
};

export default Principal;
