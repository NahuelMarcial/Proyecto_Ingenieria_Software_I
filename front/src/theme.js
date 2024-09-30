// src/theme.js
import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#ffc340", // Color principal
      dark: "#ffb300", // Color oscuro
      contrastText: "#ffffff", // Texto en botones primarios
    },
    secondary: {
      main: "#00b0ff", // Color secundario
      contrastText: "#ffffff",
    },
    background: {
      default: "#f5f5f5", // Fondo de la app
      paper: "#ffffff", // Fondo de los elementos con background de papel
    },
    text: {
      primary: "#333333", // Color principal del texto
      secondary: "#666666", // Color secundario del texto
    },
    error: {
      main: "#ff4d4d", // Color para errores
    },
    success: {
      main: "#4caf50", // Color para éxitos
    },
  },
  typography: {
    fontFamily: "Roboto, sans-serif", // Fuente principal
    h1: {
      fontSize: "2rem",
      fontWeight: "bold",
      color: "#333333",
    },
    h2: {
      fontSize: "1.5rem",
      fontWeight: "bold",
      color: "#333333",
    },
    h3: {
      fontSize: "1.17rem",
      fontWeight: "bold",
      color: "#333333",
    },
    h4: {
      fontSize: "1.17rem",
      fontWeight: "normal",
      color: "#333333",
    },
    body1: {
      fontSize: "1rem",
      fontWeight: "normal",
      color: "#666666",
    },
    button: {
      textTransform: "none", // Evita que el texto de los botones esté en mayúsculas
    },
  },
  shape: {
    borderRadius: 8, // Bordes redondeados para los elementos
  },
  spacing: 8, // Espaciado base para márgenes y padding
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 12, // Bordes redondeados en botones
          padding: "10px 20px", // Espaciado en botones
          textTransform: "none", // Mantener texto sin transformar
          boxShadow: "5px 5px 10px rgba(0, 0, 0, 0.2)", // Sombra en botones
        },
        containedPrimary: {
          backgroundColor: "#ffc340",
          color: "#fff",
          "&:hover": {
            backgroundColor: "#ffb300",
          },
        },
        containedSecondary: {
          backgroundColor: "#00b0ff",
          color: "#fff",
          "&:hover": {
            backgroundColor: "#009be5",
          },
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          padding: "16px",
          borderRadius: "12px",
          boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        },
      },
    },
  },
  shadows: [
    "none", // elevation 0
    "0px 4px 8px rgba(0, 0, 0, 0)", // elevation 1
    "5px 5px 2px rgba(0, 0, 0, 0.4)", // elevation 2
    "0px 6px 10px rgba(0, 0, 0, 0.2)", // elevation 3
    "0px 8px 12px rgba(0, 0, 0, 0.2)", // elevation 4
    "0px 10px 14px rgba(0, 0, 0, 0.2)", // elevation 5
    "0px 12px 16px rgba(0, 0, 0, 0.2)", // elevation 6
    "0px 14px 18px rgba(0, 0, 0, 0.2)", // elevation 7
    "0px 16px 20px rgba(0, 0, 0, 0.2)", // elevation 8
    "0px 18px 22px rgba(0, 0, 0, 0.2)", // elevation 9
    "0px 20px 24px rgba(0, 0, 0, 0.2)", // elevation 10
    "0px 22px 26px rgba(0, 0, 0, 0.2)", // elevation 11
    "0px 24px 28px rgba(0, 0, 0, 0.3)", // elevation 12
    "0px 26px 30px rgba(0, 0, 0, 0.3)", // elevation 13
    "0px 28px 32px rgba(0, 0, 0, 0.3)", // elevation 14
    "0px 30px 34px rgba(0, 0, 0, 0.3)", // elevation 15
    "0px 32px 36px rgba(0, 0, 0, 0.3)", // elevation 16
    "0px 34px 38px rgba(0, 0, 0, 0.3)", // elevation 17
    "0px 36px 40px rgba(0, 0, 0, 0.3)", // elevation 18
    "0px 38px 42px rgba(0, 0, 0, 0.3)", // elevation 19
    "0px 40px 44px rgba(0, 0, 0, 0.3)", // elevation 20
    "0px 42px 46px rgba(0, 0, 0, 0.3)", // elevation 21
    "0px 44px 48px rgba(0, 0, 0, 0.3)", // elevation 22
    "0px 46px 50px rgba(0, 0, 0, 0.4)", // elevation 23
    "0px 48px 52px rgba(0, 0, 0, 0.4)", // elevation 24
  ],
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 960,
      lg: 1280,
      xl: 1920,
    },
  },
});

export default theme;
