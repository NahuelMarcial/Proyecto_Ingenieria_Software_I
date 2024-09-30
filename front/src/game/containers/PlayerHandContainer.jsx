import PlayerHand from "../components/PlayerHand";
import { useEffect, useState } from "react";
import getFigCardsPlayer from "../services/getFigCardsPlayer";
import getMovCardsPlayer from "../services/getMovCardsPlayer";
import figureImages from "../services/figureImages";
import movImages from "../services/movImages";

const PlayerHandContainer = (jugador) => {
  const [figureCardsPlayer, setFigureCards] = useState([]);
  const [movCards, setMovCards] = useState([]);
  const partida_id = sessionStorage.getItem("partida_id");
  const jugador_id = jugador.jugador;

  // Determinar si el jugador es el host
  const isHost = () => {
    const storedHostId = sessionStorage.getItem("jugador_id");
    return storedHostId === jugador_id;
  };

  // Obtener las cartas de figura del jugador
  const auxFigCards = async () => {
    await getFigCardsPlayer(partida_id, jugador_id)
      .then((cards) => {
        const formattedCards = cards.map((card) => ({
          imageSrc: figureImages[card.id_carta], // diccionario para obtener la imagen
          id_carta: card.id_carta,
          title: card.nombre,
          color: card.color,
          bloqueada: card.bloqueada,
          descartada: card.descartada,
          mostrar: card.mostrar,
          reponer: card.reponer,
        }));

        setFigureCards(formattedCards);
      })
      .catch((error) => {
        console.error("Error al obtener las cartas de figura:", error);
      });
  };
  // Obtener las cartas de movimiento del jugador
  const auxMovCards = async () => {
    await getMovCardsPlayer(partida_id, jugador_id).then((cards) => {
      const formattedMovCards = cards.map((card) => ({
        imageSrc: movImages[card.id_carta], // diccionario de imágenes de movimientos
        id_carta: card.id_carta,
        title: card.tipo_movimiento,
        descartada: card.descartada,
        reponer: card.reponer,
      }));
      setMovCards(formattedMovCards);
    });
  };

  useEffect(() => {
    auxFigCards();
    auxMovCards();
  }, [partida_id, jugador]);

  return (
    <PlayerHand
      jugador_id={jugador_id}
      isHost={isHost()}
      figureCards={figureCardsPlayer}
      movCards={movCards}
    />
  );
};

export default PlayerHandContainer;
