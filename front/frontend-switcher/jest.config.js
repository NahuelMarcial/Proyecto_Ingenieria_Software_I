module.exports = {
    transform: {
      "^.+\\.(js|jsx)$": "babel-jest",
    },
    testEnvironment: "jest-environment-jsdom",
    moduleNameMapper: {
      "\\.(css|less|scss|sass)$": "identity-obj-proxy",
    },
    setupFilesAfterEnv: ["./setupTests.js"], // Asegúrate de que esta línea apunte al archivo de configuración
  };
  