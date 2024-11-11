// getWinner.test.js
import getWinner from "../game/services/getWinner";

describe("getWinner", () => {
  beforeEach(() => {
    fetch.resetMocks();
  });

  it("debe devolver el ganador cuando la respuesta es exitosa", async () => {
    const mockWinner = { id_player: "player1" };
    
    fetch.mockResponseOnce(JSON.stringify(mockWinner));

    const result = await getWinner("12345");

    expect(result).toEqual(mockWinner);
    expect(fetch).toHaveBeenCalledWith(
      expect.stringContaining("/game/12345/ganador"),
      expect.any(Object)
    );
  });

  it("debe lanzar un error cuando la respuesta no es exitosa", async () => {
    // Simular una respuesta con un código de estado no exitoso
    fetch.mockResponseOnce(JSON.stringify({ error: "Error" }), { status: 500 });
  
    await expect(getWinner("12345")).rejects.toThrow("Error al obtener el ganador");
  });
});
