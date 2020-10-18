# @iqthon c 2021
"""Pins the replied message
Syntax: .تثبيت [LOUD]"""
from telethon import events
from telethon.tl import functions, types
from userbot.utils import admin_cmd


@borg.on(admin_cmd("تثبيت ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    silent = True
    input_str = event.pattern_match.group(1)
    if input_str:
        silent = False
    if event.message.reply_to_msg_id is not None:
        message_id = event.message.reply_to_msg_id
        try:
            await borg(functions.messages.UpdatePinnedMessageRequest(
                event.chat_id,
                message_id,
                silent
            ))
        except Exception as e:
            await event.edit(str(e))
        else:
            await event.delete()
    else:
        await event.edit("قم برد على الرساله لتثبيته في القناه او المجموعه.")
