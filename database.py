import motor.motor_asyncio
from model import Game

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb+srv://faysalewucse:DotDoWsIcZLSR4Q8@sportx.kehzdkr.mongodb.net/sportx')
database = client.sportx
collection = database.games


async def fetch_paired_teams():
    cursor = collection.find({"homepage_x": "ts"})

    # Fetch and convert games
    games = []
    async for document in cursor:
        game_data = {**document, 'id': str(document['_id'])}
        games.append(Game(**game_data))

    # Pair teams logic
    paired_teams = [
        games[i:i + 2] for i in range(0, len(games), 2)
    ]

    return paired_teams


async def fetch_teams():
    cursor = collection.find({"$expr": {"$eq": ["$team", "$sp_name"]}})

    # Fetch and convert games
    games = []
    async for document in cursor:
        game_data = {**document, 'id': str(document['_id'])}
        games.append(Game(**game_data))

    return games


async def fetch_first_game():
    document = await collection.find_one()
    paired_teams = await fetch_paired_teams()
    if document:
        game_data = {**document, 'id': str(document['_id'])}
        return {"firstGame": Game(**game_data), "pairedTeams": paired_teams}
    return {}


async def fetch_games_by_sp_id(sp_id: int):
    games = []
    cursor = collection.find({"sp_id": sp_id})
    async for document in cursor:
        game_data = {**document, 'id': str(document['_id'])}
        games.append(Game(**game_data))
    return games


async def fetch_all_games():
    games = []
    cursor = collection.find()
    async for document in cursor:
        game_data = {**document, 'id': str(document['_id'])}
        games.append(Game(**game_data))
    return games
