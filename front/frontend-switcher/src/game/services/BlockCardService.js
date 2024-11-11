import UrlAPI from "../../configs/urlAPI";

const blockCardService = async (game_id, id_bloqueador, id_carta, id_ficha) => {
  try {
    const Url_block =
      UrlAPI + "/game/" + game_id + "/carta_figura/bloquear_carta/";
    const body = {
      id_bloqueador: id_bloqueador,
      id_carta: id_carta,
      id_ficha: id_ficha,
    };

    console.log("body", body);
    const response = await fetch(Url_block, {
      method: "PATCH",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      throw new Error("Error al bloquear carta de figura");
    }
  } catch (e) {
    throw e;
  }
};

export default blockCardService;
