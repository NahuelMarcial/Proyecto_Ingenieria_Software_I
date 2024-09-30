// Logica para crear una partida
import { createGameService } from "./createGameService";

export const handleCreateGame = async (formData, setLoading, handleClose) => {
  setLoading(true);

  // Datos a enviar al servidor
  const dataToSend = {
    ...formData,
    owner: sessionStorage.getItem("jugador_id"),
    sid: sessionStorage.getItem("sid"),
    max_jugadores: parseInt(formData.max_jugadores, 10),
  };

  console.log("Datos enviados:", dataToSend);

  try {
    console.log(JSON.stringify(dataToSend));
    const dataGame = await createGameService(dataToSend);
    try {
      // guardar cualquier dato necesario en el sessionStorage
      console.log("Datos de la partida:", dataGame);
      sessionStorage.setItem("partida_id", dataGame.id);
      sessionStorage.setItem("partida_nombre", dataGame.nombre);
    } catch (error) {
      console.error("Error al guardar los datos de la partida:", error);
    } finally {
    }

    console.log("Partida creada con éxito");
    handleClose(); // cerrar el formulario
  } catch (error) {
    console.error("Error al crear la partida: partida no creada", error);
  } finally {
    setLoading(false);
  }
};
