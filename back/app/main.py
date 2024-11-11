from app.create_app import create_app
from app.home.app import router as home_router
from app.lobby.app import router as lobby_router
from app.game.app import router as game_router
from app.database.database import create_all

create_all()

app = create_app()

app.include_router(home_router, prefix="/home")
app.include_router(lobby_router, prefix="/lobby/{partida_id}")
app.include_router(game_router, prefix="/game/{partida_id}")

@app.get("/")
def root():
    return {"Hola soy un test"}