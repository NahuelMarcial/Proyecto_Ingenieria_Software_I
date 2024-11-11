import UrlAPI from "../../configs/urlAPI"

const urlgameActive = UrlAPI + "/home/partidas_activas/";

const gameEntryActiveService = async (player_id) => {
	try {
		const response = await fetch(urlgameActive + player_id, {
			method: "GET",
			headers: {'accept': 'application/json'}
		})
		if (!response.ok) {
			throw new Error("Error al obtener las partidas activas")
		}
		return await response.json();
	} catch (e) {
		throw e;
	}
};

export default gameEntryActiveService;