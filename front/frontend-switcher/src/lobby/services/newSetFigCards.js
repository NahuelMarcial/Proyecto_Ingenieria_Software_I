import URL_API from "../../configs/urlAPI";

export const newSetFigCards = async (partida_id) => {
  try {
    const response = await fetch(
      URL_API + `/game/${partida_id}/carta_figura/set`,
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
