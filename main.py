from fastapi import FastAPI, HTTPException
import uvicorn

from database import (
    fetch_all_games,
    fetch_first_game,
    fetch_teams,
    fetch_games_by_sp_id
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://sportx-artif.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return "Server is Running"


@app.get("/api/games")
async def get_all_games():
    response = await fetch_all_games()
    return response


@app.get("/api/games/{sp_id}")
async def get_all_games(sp_id: int):
    response = await fetch_games_by_sp_id(sp_id)
    return response


@app.get("/api/games/teams")
async def get_all_teams():
    response = await fetch_teams()
    return response


@app.get("/api/games/first-game")
async def get_first_game():
    response = await fetch_first_game()
    return response


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
# @app.get("/api/games/{year}")
# async def get_todo(year: int):
#     response = await fetch_all_games(year)
#     return response
