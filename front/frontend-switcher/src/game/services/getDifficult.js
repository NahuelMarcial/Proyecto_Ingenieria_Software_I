import URL_API from "../../configs/urlAPI";

const getDifficult = async () => {
  try {
    const partida_id = sessionStorage.getItem("partida_id");
    const response = await fetch(`${URL_API}/home/partida/${partida_id}`);
    const data = await response.json();
    return data.dificil;
  } catch (error) {
    console.error("Error al obtener la dificultad:", error);
    return;
  }
};

export default getDifficult;
