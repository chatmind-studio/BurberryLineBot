from typing import Any, Optional

from dotenv import load_dotenv
from line import Bot, Cog, Context, command
from line.models import ButtonsTemplate, Emoji, PostbackAction

from burberry_bot.crawl import convert_currency, get_item_price

load_dotenv()


class Commands(Cog):
    def __init__(self, bot: Bot):
        super().__init__(bot)
        self.bot = bot

    @command
    async def compare_price(self, ctx: Context, url: Optional[str] = None) -> Any:
        if not url:
            template = ButtonsTemplate(
                "Burberry 商品台日比價",
                actions=[
                    PostbackAction(
                        data="ignore",
                        label="按我貼上商品網址",
                        display_text="請貼上台灣 Burberry 官網的商品網址",
                        input_option="openKeyboard",
                        fill_in_text="cmd=compare_price&url=",
                    )
                ],
            )
            await ctx.reply_template("台日比價", template=template)
        else:
            tw_price = await get_item_price(url)
            jp_price = await get_item_price(
                url.replace("tw.burberry.com", "jp.burberry.com")
            )
            converted_jp_price = round(await convert_currency(jp_price))
            price_diff = tw_price - converted_jp_price
            discount = str(round(converted_jp_price / tw_price * 100)).replace("0", "")
            text = f"台灣購買價格為 {tw_price} 台幣\n日本購買價格為 {jp_price} 日圓\n(約 {converted_jp_price} 台幣)"
            if price_diff > 0:
                await ctx.reply_text(
                    f"{text}\n日本比台灣便宜 {price_diff} 台幣\n約打 {discount} 折"
                )
            else:
                await ctx.reply_text(f"{text}\n台灣比日本便宜 {-price_diff} 台幣\n建議在台灣購買!")

    @command
    async def steps(self, ctx: Context) -> Any:
        await ctx.reply_text(
            "長住日本東京新宿，可開台灣蝦皮賣場保障交易安全，如需日本代購郵寄服務 (不限Burberry商品), 請按 https://line.me/ti/p/saJrohf7wx 加 $ 好友聊聊，我們會盡快與您聯繫 $",
            emojis=[
                Emoji("5ac21a18040ab15980c9b43e", "014"),
                Emoji("5ac1bfd5040ab15980c9b435", "215"),
            ],
        )

    @command
    async def help(self, ctx: Context) -> Any:
        await ctx.reply_text(
            "1. 點擊「Burberry 台灣官網」\n2. 搜尋你想要的商品\n3. 複製商品網址\n4. 點擊「台日比價」\n5. 貼上商品網址"
        )
