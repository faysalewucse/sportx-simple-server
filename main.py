from fastapi import FastAPI, HTTPException

from database import (
    fetch_all_games,
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


@app.get("/api/games/{year}")
async def get_todo(year: int):
    response = await fetch_all_games(year)
    return response
