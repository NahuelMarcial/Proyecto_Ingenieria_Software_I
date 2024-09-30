export const newSetFigCards = async (partida_id) => {
  try {
    const response = await fetch(
      `http://localhost:8000/carta_figura/set/${partida_id}`,
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
        "No se pudo asignar un set de cartas figura a la partida " + partida_id
      );
    }
    let setFigureCards = await response.json();
    return setFigureCards;
  } catch (error) {
    console.error("Error: newSetFigCards.", error);
    throw error;
  }
};

export default newSetFigCards;
