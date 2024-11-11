import React from "react";
import {render, screen} from "@testing-library/react";
import PlayerCard from "../lobby/components/PlayerCard";
import getFaceIcon from "../lobby/components/Faces";
import {ThemeProvider, createTheme} from "@mui/material/styles";
import "@testing-library/jest-dom";

// Creamos un mock de getFaceIcon para controlar su resultado en los tests
jest.mock("../lobby/components/Faces.jsx", () => jest.fn());

const theme = createTheme();

describe("PlayerCard component", () => {
  beforeEach(() => {
    getFaceIcon.mockClear(); // Limpiar mock entre tests
  });

  it("deberia mostrar 'Disponible' cuando no hay un jugador ocupando la tarjeta, pero no lo hace.", () => {
    render(
      <ThemeProvider theme={theme}>
        <PlayerCard player={null} name="Player Name" face={1}/>
      </ThemeProvider>
    );

    // Verificamos que el texto "Disponible" se muestre
    expect(screen.getByText("Disponible")).toBeInTheDocument();
  });

  it("deberia mostrar el nombre del jugador cuando hay un jugador ocupando la tarjeta, pero no lo hace.", () => {
    render(
      <ThemeProvider theme={theme}>
        <PlayerCard player={{id: 1}} name="John Doe" face={1}/>
      </ThemeProvider>
    );

    // Verificamos que el nombre del jugador se muestre
    expect(screen.getByText("John Doe")).toBeInTheDocument();
  });

  it("deberia mostrar el ícono de cara correspondiente al 'face' pasado como prop, pero no lo hace.", () => {
    getFaceIcon.mockReturnValue(<div data-testid="face-icon"/>); // Mock de retorno

    render(
      <ThemeProvider theme={theme}>
        <PlayerCard player={{id: 1}} name="Jane Doe" face={2}/>
      </ThemeProvider>
    );

    // Verificamos que se llama a getFaceIcon con el valor correcto
    expect(getFaceIcon).toHaveBeenCalledWith(2, true);
    expect(screen.getByTestId("face-icon")).toBeInTheDocument();
  });

  it("deberia mostrar el icono de estrella cuando es el owner y el jugador ocupa la tarjeta, pero no lo hace", () => {
    render(
      <ThemeProvider theme={theme}>
        <PlayerCard player={{id: 1}} name="Player Star" face={0}/>
      </ThemeProvider>
    );

    // Verificamos que se muestre el ícono de estrella
    expect(screen.getByTestId("CrownIcon")).toBeInTheDocument();
  });
});
