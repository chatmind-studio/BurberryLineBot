import asyncio
import os

from dotenv import load_dotenv

from burberry_bot.bot import BurberryBot


async def main() -> None:
    load_dotenv()
    channel_secret = os.getenv("LINE_CHANNEL_SECRET")
    access_token = os.getenv("LINE_ACCESS_TOKEN")
    if not (channel_secret and access_token):
        raise RuntimeError("LINE_CHANNEL_SECRET and LINE_ACCESS_TOKEN are required.")

    bot = BurberryBot(channel_secret, access_token)
    await bot.run()


asyncio.run(main())
