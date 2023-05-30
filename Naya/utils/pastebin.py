"""
MIT License
Copyright (c) 2023 Kynan | TheHamkerCat

"""
from Naya.utils.http import post

BASE = "https://batbin.me/"


async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]
