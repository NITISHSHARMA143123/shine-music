from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import GROUP_USERNAME, CHANNEL_USERNAME


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💫ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ❣️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚡ғᴇᴀᴛᴜʀᴇ⚡",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="👉🏻sᴇᴛᴛɪɴɢ👈🏻", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("{BOT_USERNAME}")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    global GROUP_USERNAME
    global CHANNEL_USERNAME
    buttons = [
        [
            InlineKeyboardButton(
                text="💫ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ❣️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="ᴍᴏʀᴇ🥀", url=f"https://t.me/{CHANNEL_USERNAME}",
            ),
        
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ✨", url=f"https://t.me/{GROUP_USERNAME}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⚡Ғᴇᴀᴛᴜʀᴇs⚡", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
