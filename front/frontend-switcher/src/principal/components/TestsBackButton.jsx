import React, { useState } from "react";
import { BackToGame, BackToLobby } from "../components/BackToButtons";

const TestComponent = () => {
  const [partidaId, setPartidaId] = useState(1);
  const partidaNombre = "abc123"; // Puedes cambiarlo según tus necesidades

  return (
    <div>
      <label htmlFor="partidaId">Partida ID:</label>
      <input
        type="number"
        id="partidaId"
        value={partidaId}
        onChange={(e) => setPartidaId(e.target.value)}
        style={{ margin: "0 10px" }}
      />

      <BackToLobby
        partidaId={Number(partidaId)}
        partidaNombre={partidaNombre}
      />
      <BackToGame partidaId={Number(partidaId)} partidaNombre={partidaNombre} />
    </div>
  );
};

export default TestComponent;
