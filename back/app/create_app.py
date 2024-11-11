from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.sockets.socket_connection import sio_app
import app.sockets.socket_chat

def create_app() -> FastAPI:
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

    return app