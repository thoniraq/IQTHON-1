
"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "IQTHON"
CAT_IMG = Config.ALIVE_PIC

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("⌔︙🕷🇮🇶 IRAQTHON\n"
                     "⌔︙🕷🇮🇶 Version: 1.0.0\n"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                      "⌔︙🕷🇮🇶 Created By: [KLANR](tg://user?id=1094825801) || [CH IQ](https://t.me/IQTHON)\n"
                     f"⌔︙🕷🇮🇶 My Master : {DEFAULTUSER}\n")
                     
