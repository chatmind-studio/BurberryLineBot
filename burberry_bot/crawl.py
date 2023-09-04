import aiohttp
from bs4 import BeautifulSoup


async def get_item_price(url: str) -> int:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            soup = BeautifulSoup(await resp.text(), "html.parser")
            price = soup.find("div", class_="product-info-panel__price").text  # type: ignore
            price = price.replace("TWD", "").replace("¥", "")
            return int(price.split(".")[0].replace(",", ""))


async def convert_currency(amount: int) -> int:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.exchangerate-api.com/v4/latest/TWD"
        ) as resp:
            rates = await resp.json()
            return amount / rates["rates"]["JPY"]
