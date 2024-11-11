import URL_API from "../../configs/urlAPI";

export const restoreMessages = async (partida_id) => {
  const API_URL = URL_API + `/game/${partida_id}/chat_restore`;
  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error("Error obteniendo los mensajes");
    }
    return;
  } catch (error) {
    console.error("Error fetching mensajes:", error);
    throw error;
  }
};

export default restoreMessages;
