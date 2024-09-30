from fastapi import FastAPI
from app.partida.app import router as partida_router
from app.lobby.app import router as lobby_router
from app.carta_figura.app import router as carta_figura_router
from app.carta_movimiento.app import router as carta_movimiento_router
from app.game.app import router as game_router
from app.fichas.app import router as fichas_router
from app.database.database import create_all
from fastapi.middleware.cors import CORSMiddleware
from app.sockets.socket_connection import sio_app

create_all()

app = FastAPI()

app.mount("/sockets", sio_app)

origins = ["*"]  # Permisos para acceder a la API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(partida_router, prefix="/partida")
app.include_router(lobby_router, prefix="/lobby")
app.include_router(game_router, prefix="/game")
app.include_router(carta_figura_router, prefix="/carta_figura")
app.include_router(carta_movimiento_router, prefix="/carta_movimiento")
app.include_router(fichas_router, prefix="/fichas")
@app.get("/")
def root():
    return {"Hola soy un test"}