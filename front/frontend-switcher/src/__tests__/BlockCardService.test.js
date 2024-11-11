import BlockCardService from "../game/services/BlockCardService";
import URL_API from "../configs/urlAPI";

describe("Test Block card Service", () => {
  const mockgameid = 0;
  const mockblockerid = 1;
  const idcarta = 3;
  const idficha = 4;
  beforeEach(() => {
    global.fetch = jest.fn();
  });
  afterEach(() => {
    jest.clearAllMocks();
  });

  it("Se realiza el fetch sin ocurrencia de errores", async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({}),
    });
    await BlockCardService(mockgameid, mockblockerid, idcarta, idficha);
    expect(global.fetch).toHaveBeenCalledWith(
      `${URL_API}/game/${mockgameid}/carta_figura/bloquear_carta/`,
      {
        method: "PATCH",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id_bloqueador: mockblockerid,
          id_carta: idcarta,
          id_ficha: idficha,
        }),
      }
    );
  });

  it("Se realiza el fetch con ocurrencia de errores", async () => {
    global.fetch.mockResolvedValueOnce({
      ok: false,
    });
    await expect(
      BlockCardService(mockgameid, mockblockerid, idcarta, idficha)
    ).rejects.toThrow("Error al bloquear carta de figura");
  });
});
