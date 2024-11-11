import URL_API from "../../configs/urlAPI";

export const getOwner = async (partida_id) => {
  try {
    const response = await fetch(URL_API + `/lobby/${partida_id}/owner`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error en getOwner:", error);
  }
};

export default getOwner;
