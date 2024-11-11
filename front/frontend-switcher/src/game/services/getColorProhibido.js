import URL_API from "../../configs/urlAPI";

const getColorProhibido = async () => {
		try {
			const partida_id = sessionStorage.getItem("partida_id")
			const response = await fetch(URL_API + `/game/${partida_id}/color_prohido`,
				{
					method: "GET",
					headers:
						{
							'accept':
								'application/json'
						}
				}
			)
			if (!response.ok) {
				throw new Error("Error al obtner el nuevo color prohiido");
			}
			return await response.json();
		} catch
			(e) {
			throw (e)
		}
	}
;

export default getColorProhibido;