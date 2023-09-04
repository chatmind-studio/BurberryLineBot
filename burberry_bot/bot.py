import logging

from line import Bot

from .rich_menu import RICH_MENU


class BurberryBot(Bot):
    def __init__(self, channel_secret: str, access_token: str) -> None:
        super().__init__(channel_secret=channel_secret, access_token=access_token)

    async def _setup_rich_menu(self) -> None:
        result = await self.line_bot_api.create_rich_menu(RICH_MENU)
        with open("data/rich_menu.png", "rb") as f:
            await self.blob_api.set_rich_menu_image(
                result.rich_menu_id,
                body=bytearray(f.read()),
                _headers={"Content-Type": "image/png"},
            )
        await self.line_bot_api.set_default_rich_menu(result.rich_menu_id)

    async def setup_hook(self) -> None:
        logging.info("Adding cog")
        self.add_cog("burberry_bot.cmds")
        logging.info("Setting up rich menu")
        await self._setup_rich_menu()
