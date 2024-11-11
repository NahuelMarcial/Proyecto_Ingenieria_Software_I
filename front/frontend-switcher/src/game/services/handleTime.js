import { useState, useEffect } from "react";
import { getStartTurnTime, endTurnTimeOut } from "./turnoService";
import emitter from "./eventEmitter";

const TURN_DURATION = 121 * 1000;

export const useHandleTime = (socket) => {
  const [time, setTime] = useState(120);
  const [timeIsEnding, setTimeIsEnding] = useState(false);
  const partida_id = sessionStorage.getItem("partida_id");
  const [uniqueLog, setUniqueLog] = useState(false);

  const handleSessionTime = async () => {
    if (!sessionStorage.getItem("turnStartTime")) {
      const startTime = await getStartTurnTime(partida_id);
      sessionStorage.setItem("turnStartTime", startTime);
    }
  };

  const handleTime = () => {
    const startTime = sessionStorage.getItem("turnStartTime");
    if (!startTime) return;

    const currentTime = Date.now();
    const timeElapsed = currentTime - startTime;
    const timeLeft = TURN_DURATION - timeElapsed;

    setTime(Math.max(Math.floor(timeLeft / 1000), 0));
    setTimeIsEnding(timeLeft <= 10000);

    if (timeLeft <= 900) {
      const response = endTurnTimeOut(partida_id);
      if (!response.ok) {
        sessionStorage.removeItem("turnStartTime");
        handleSessionTime();
      }
      if (!uniqueLog) {
        emitter.emit("log_TiempoAgotado");
        setUniqueLog(true);
      }
    }
  };

  useEffect(() => {
    handleSessionTime();
    handleTime();

    const intervalId = setInterval(handleTime, 1000);

    socket.on("turno_pasado", () => {
      sessionStorage.removeItem("turnStartTime");
      handleSessionTime();
      handleTime();
    });

    return () => {
      clearInterval(intervalId);
      socket.off("turno_pasado");
    };
  }, [socket]);

  return { time, timeIsEnding };
};
