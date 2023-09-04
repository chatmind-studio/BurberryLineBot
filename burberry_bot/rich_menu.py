from line.models import MessageAction, URIAction
from linebot.v3.messaging import (
    RichMenuArea,
    RichMenuBounds,
    RichMenuRequest,
    RichMenuSize,
)

RICH_MENU = RichMenuRequest(
    size=RichMenuSize(width=1200, height=810),
    selected=True,
    name="rich_menu",
    chatBarText="點擊開啟/關閉選單",
    areas=[
        RichMenuArea(
            bounds=RichMenuBounds(x=400, y=0, width=800, height=405),
            action=MessageAction(text="cmd=compare_price", label="台日比價"),
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=400, height=405),
            action=URIAction(
                uri="https://tw.burberry.com/?openExternalBrowser=1", label="台灣官網"
            ),
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=405, width=400, height=405),
            action=URIAction(
                uri="https://line.me/R/nv/recommendOA/%40995ubkon", label="好用請分享"
            ),
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=400, y=405, width=400, height=405),
            action=MessageAction(text="cmd=help", label="使用說明"),
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=800, y=405, width=400, height=405),
            action=MessageAction(text="cmd=steps", label="代購流程"),
        ),
    ],
)
