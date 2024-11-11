import React, { useState } from "react";
import {
  TextField,
  Typography,
  Box,
  IconButton,
  Collapse,
  Button,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search"; // icono de lupa

const SearchGames = ({ availableGames, onFilter }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedPlayers, setSelectedPlayers] = useState([]);
  const [isExpanded, setIsExpanded] = useState(false);

  // Función para alternar la selección de botones de número de jugadores
  const togglePlayerSelection = (playerCount) => {
    setSelectedPlayers((prevSelected) => {
      if (prevSelected.includes(playerCount)) {
        return prevSelected.filter((num) => num !== playerCount);
      } else {
        return [...prevSelected, playerCount];
      }
    });
  };

  // Función para filtrar las partidas por nombre y número de jugadores seleccionados
  const filterGames = (term, players) => {
    const filteredGames = availableGames.filter((game) => {
      const matchByName = game.nombre
        .toLowerCase()
        .includes(term.toLowerCase());
      const matchByPlayers =
        players.length === 0 || players.includes(game.cantidad_jugadores);

      return matchByName && matchByPlayers;
    });

    onFilter(filteredGames);
  };

  // Se ejecuta cuando cambia el valor en el campo de búsqueda de nombre
  const handleSearchByName = (e) => {
    const term = e.target.value;
    setSearchTerm(term);
    filterGames(term, selectedPlayers);
  };

  // Se ejecuta cuando cambia la selección de botones de cantidad de jugadores
  const handlePlayerButtonClick = (playerCount) => {
    togglePlayerSelection(playerCount);
    filterGames(
      searchTerm,
      selectedPlayers.includes(playerCount)
        ? selectedPlayers.filter((num) => num !== playerCount)
        : [...selectedPlayers, playerCount]
    );
  };

  // Función para manejar la expansión del collapse
  const handleExpand = () => {
    setIsExpanded((prev) => !prev);
  };

  const searchBox = (
    <Box
      elevation={0}
      sx={{
        width: "100%",
        height: "10vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        backgroundColor: "#f8f9fa",
      }}
    >
      <IconButton
        onClick={handleExpand}
        sx={{
          backgroundColor: "secondary.main", // Cambia el fondo al color secundario
          color: "#ffffff", // Hace que el icono sea blanco
          "&:hover": {
            backgroundColor: "secondary.dark", // Color de fondo al pasar el mouse
          },
          marginRight: { xs: 0.5, sm: 1 },
          "& .MuiSvgIcon-root": {
            fontSize: isExpanded ? { xs: 24, sm: 30, md: 36 } : 36, // Cambia el tamaño del icono
            transition: "font-size 0.5s ease", // Transición suave para el cambio de tamaño
          }
        }}
      >
        <SearchIcon sx={{ fontSize: 36 }} />
      </IconButton>
      <Box
        sx={{
          width: { xs: 50, sm: 136, md: 220},
          marginRight: { xs: 0.5, sm: 1 },
        }}
      >
        <TextField
          label="Buscar por Nombre"
          variant="outlined"
          color="secondary"
          value={searchTerm}
          onChange={handleSearchByName}
          sx={{ 
            minWidth: "100%",  
          }}
        />

      </Box>
      <Box
        sx={{
          display: "flex-end",
          flexDirection: "column",
          alignItems: "center",
          paddingBottom: 1.5,
        }}
      >
        <Typography 
          variant="caption"
          color="secondary"
          fontSize="clamp(0.7rem, 1.2vw, 1rem)"
        >
          Buscar por Jugadores
        </Typography>
        <Box sx={{ display: "flex", gap: { xs: 0.5, sm:0.8, md:1 } }}>
          {[1, 2, 3].map((number) => (
            <Button
              key={number}
              sx={{
                width: { xs: 28, sm: 45, md: 60, lg: 70 },
                height: { xs: 25, sm: 35, md: 45, lg: 50 },
                fontSize: { xs: 12, sm: 16, md: 20 },
                fontWeight: "bold",
                padding: 0,
                minWidth: "auto",
              }}
              variant={
                selectedPlayers.includes(number) ? "contained" : "outlined"
              }
              color="secondary"
              onClick={() => handlePlayerButtonClick(number)}
            >
              {number}
            </Button>
          ))}
        </Box>
      </Box>
    </Box>
  );

  return (
    <div>
      <Collapse
        orientation="horizontal"
        in={isExpanded}
        collapsedSize={52}
        timeout={500}
        sx={{
          marginRight: 1,
          transition: "all 0.5s ease", // Transición fluida para todo el colapso
        }}
      >
        {searchBox}
      </Collapse>
    </div>
  );
};

export default SearchGames;
