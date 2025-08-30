import requests

CHESS_API_BASE_URL = "https://api.chess.com/pub"

def get_player_profile(username:str) -> dict:
    """Fetches the profile of a chess player by username."""
    url = f"{CHESS_API_BASE_URL}/player/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_player_stats(username:str) -> dict:
    """Fetches the statistics of a chess player by username."""
    url = f"{CHESS_API_BASE_URL}/player/{username}/stats"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()