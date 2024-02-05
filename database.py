import motor.motor_asyncio
from model import Game

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb+srv://faysalewucse:DotDoWsIcZLSR4Q8@sportx.kehzdkr.mongodb.net/sportx')
database = client.sportx
collection = database.games


async def fetch_all_games(year: int):
    games = []
    cursor = collection.find({"sea": year})
    async for document in cursor:
        game_data = {**document, 'id': str(document['_id'])}
        print(game_data)
        games.append(Game(**game_data))
    return games

