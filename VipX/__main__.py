import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from VipX import LOGGER, app, userbot
from VipX.core.call import Vip
from VipX.plugins import ALL_MODULES
from VipX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VipX").error(
            "sᴛʀɪɴɢ sᴇssɪᴏɴ ᴋᴏɴ ᴛᴇʀᴀ ʙᴀᴀᴘ ᴅᴀʟᴇɢᴀ ʙsᴅᴋ"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("VipX").warning(
            "sᴘᴏᴛɪғʏ ɪᴅ ᴘᴀᴘᴀ ᴀᴀʏᴇɢᴇ ᴅᴀʟɴᴇ ʙsᴅᴋ"
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VipX.plugins." + all_module)
    LOGGER("VipX.plugins").info(
        "ᴄʜᴀʟ ʜᴏ ɢʏᴀ sᴀʙ"
    )
    await userbot.start()
    await Vip.start()
    await Vip.decorators()
    LOGGER("VipX").info("╚╔×═════•۩∆۩•════×╗╝\n ✨𝐕𝐄𝐍𝐎𝐌⚡\n╚╔×═════•۩∆۩•════×╗╝")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("VipX").info("ᴍᴀᴀ ᴄʜᴜᴅ ɢʏɪ ʙᴏᴛ ᴋɪ ᴇʀʀᴏʀ ғɪx ᴋᴀʀ ᴊᴀʟᴅɪ")
