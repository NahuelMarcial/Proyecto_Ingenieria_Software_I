export const newSetMovCards = async (partida_id) => {
  try {
    const response = await fetch(
      `http://localhost:8000/carta_movimiento/set/${partida_id}`,
      {
        method: "POST",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    );
    if (response.ok !== true) {
      throw new Error(
        "No se pudo asignar un set de cartas de movimiento a la partida " +
          partida_id
      );
    }
    let setFigureCards = await response.json();
    return setFigureCards;
  } catch (error) {
    console.error("Error: newSetMovCards.", error);
    throw error;
  }
};

export default newSetMovCards;
