const deleteGame = async (partida_id, sid) => {
  const response = await fetch(
    `http://localhost:8000/game/eliminar/` + partida_id + "/" + sid,
    {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: sid,
      },
    }
  );

  const respuesta = response.json();
  return response;

  if (response.status === 200) {
    return true;
  } else {
    return false;
  }
};

export default deleteGame;
