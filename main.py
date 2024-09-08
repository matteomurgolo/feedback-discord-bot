import os
from dotenv import load_dotenv
from bot.client import get_discord_client

load_dotenv()

if __name__ == "__main__":
    client = get_discord_client()
    client.run(os.getenv('DISCORD_BOT_TOKEN'))
