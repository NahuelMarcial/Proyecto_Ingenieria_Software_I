export const getOwner = async (partida_id) => {
  try {
    const response = await fetch(
      `https://proyecto-ingenieria-software-i.onrender.com/lobby/owner/${partida_id}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error en getOwner:", error);
  }
};

export default getOwner;
