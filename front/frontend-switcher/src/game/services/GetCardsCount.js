import URL_API from "../../configs/urlAPI";

const GetCardsCount = async (game_id, player_id) => {
	try {
		const Url_AmmountCards = URL_API + "/game/" + game_id + "/carta_figura/cartas_restantes/" + player_id;
		const response = await fetch(Url_AmmountCards, {
			method: "GET",
			headers: {'accept': 'application/json'}
		})
		if (!response.ok) {
			throw new Error("Error al obtener cantidad de cartas del jugador");
		}
		return await response.json();

	} catch (e) {
		throw e;
	}
};

export default GetCardsCount;