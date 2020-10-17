"""Restart or Terminate the bot from any chat
Available Commands:
.اعاده تشغيل
.ايقاف تشغيل"""
# @iqthon c 2021
from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd


@borg.on(admin_cmd("اعاده تشغيل"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("جاري اعاده تشغيل عراق ثون انتضر 5 دقائق رجاء ثم ارسل .بنك")
    # await asyncio.sleep(2)
    # await event.edit("التاكد اذا كان لديك انترنيت انتضر.")
    # await asyncio.sleep(2)
    await event.edit("تم الاستئناف ارسل .alive")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd("ايقاف تشغيل"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("تم ايقاف تشغيل في حاله اردت تشغيله قم بذهاب الى هيروكو وتشغيل النقطه الى الازرق")
    await borg.disconnect()
