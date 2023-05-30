"""
MIT License
Copyright (c) 2023 Kynan | TheHamkerCat

"""
from pyrogram import filters

from Naya import app
from Naya.core.decorators.errors import capture_err
from Naya.utils.http import get

__MODULE__ = "Repo"
__HELP__ = "/repo - To Get My Github Repository Link " "And Support Group Link"


@app.on_message(filters.command("repo"))
@capture_err
async def repo(_, message):
    users = await get(
        "https://api.github.com/repos/naya1503/NayaRobot/contributors"
    )
    list_of_users = "".join(
        f"**{count}.** [{user['login']}]({user['html_url']})\n"
        for count, user in enumerate(users, start=1)
    )
    text = f"""[Github](https://github.com/naya1503/NayaRobot) | [Group](t.me/kynansupport)
```----------------
| Contributors |
----------------```
{list_of_users}"""
    await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
