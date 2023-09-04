import argparse
import asyncio
import os

from dotenv import load_dotenv

from burberry_bot.bot import BurberryBot

port = argparse.ArgumentParser()
port.add_argument("--port", type=int, default=7000)
args = port.parse_args()


async def main() -> None:
    load_dotenv()
    channel_secret = os.getenv("LINE_CHANNEL_SECRET")
    access_token = os.getenv("LINE_ACCESS_TOKEN")
    if not (channel_secret and access_token):
        raise RuntimeError("LINE_CHANNEL_SECRET and LINE_ACCESS_TOKEN are required.")

    bot = BurberryBot(channel_secret, access_token)
    await bot.run(port=args.port)


asyncio.run(main())
