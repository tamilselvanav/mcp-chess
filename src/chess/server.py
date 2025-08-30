from mcp.server.fastmcp import FastMCP
from .chess_api import get_player_profile, get_player_stats

mcp = FastMCP("Chess")

@mcp.tool()
def get_player_profile(username: str) -> dict:
    """Fetches the profile of a chess player by username."""
    return chess_api.get_player_profile(username)

@mcp.tool()
def get_player_stats(username: str) -> dict:
    """Fetches the statistics of a chess player by username."""
    return chess_api.get_player_stats(username)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
