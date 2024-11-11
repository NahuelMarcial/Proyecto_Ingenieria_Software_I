import React, { useEffect } from "react";
import CreateGameContainer from "./CreateGameContainer";
import GameListContainer from "./GameList";
import GameEntryActiveList from "./GameEntryActiveList";
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
          body: { margin: 0, padding: 0, height: "90%" },
        }}
      />
      <Box
        display="flex"
        alignItems="center"
        justifyContent="space-between"
        bgcolor="#FAFAEB" // Fondo oscuro del tema
        padding={2} // Añade padding interno
        borderRadius={2} // Bordes redondeados
        maxWidth="87%"
        margin="0 auto" // Centra horizontalmente la Box en la página
        marginTop={2} // Añade margen superior
        marginBottom={2} // Añade margen inferior
      >
        <Typography
          variant="h1"
          color="primary"
          sx={{
            marginRight: {
              xs: 2,
              sm: 4,
            },
            display: "flex", // Hace que el texto se ajuste en una sola línea
            flexWrap: "wrap", // Permite el ajuste de texto en líneas cuando sea necesario
            whiteSpace: {
              xs: "normal", // Permite salto de línea en pantallas pequeñas
              md: "nowrap", // Impide salto de línea en pantallas medianas y mayores
            },
          }}
        >
          BIENVENIDO AL&nbsp;{" "}
          <span style={{ display: "block" }}> "SWITCHER ONLINE"</span>
        </Typography>
        <Box marginRight="5%">
          <CreateGameContainer />
        </Box>
      </Box>
      <Box display="flex" margin="0 auto" gap={2} sx={{ width: "90%" }}>
        <Box flex={5} width="100%">
          <GameListContainer socket={socket} />
        </Box>
        <Box flex={3}>
          <GameEntryActiveList socket={socket} />
        </Box>
      </Box>
      <SetNickname />
    </div>
  );
};

export default Principal;
