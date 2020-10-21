# @iqthon c 2021
"""Emoji

Available Commands:

.رفع وهمي"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "رفع وهمي":

        await event.edit(input_str)

        animation_chars = [
        
            "**Promoting User As Admin...**",
            "**Enabling All Permissions To User...**",
            "**(1) صلاحيه : ☑️**",
            "**(1) تم اعطائه صلاحيه: ✅**",
            "**(2) ارسال وسائط: ☑️**",
            "**(2) تم اعطائه صلاحيه الوسائط: ✅**",
            "**(3) ارسال ملصقات: ☑️**",
            "**(3) تم اعطائه صلاحيه ملصقات: ✅**",    
            "**(4) ارسال استطلاع: ☑️**",
            "**(4) تم اعطائه صلاحيه استطلاع: ✅**",
            "**(5) ارسال روابط: ☑️**",
            "**(5) تم اعطائه صلاحيه روابط: ✅**",
            "**(6) اضافه اعضاء: ☑️**",
            "**(6) تم اعطائه صلاحيه اضافه: ✅**",
            "**(7) تثبيت رسائل: ☑️**",
            "**(7) تم اعطائه صلاحيه التثبيت: ✅**",
            "**(8)معلومات مجموعه: ☑️**",
            "**(8) تم وصول معلومات مجموعه: ✅**",
            "**تم منح الاذن بنجاح**",
            "**تابع قناتنا @IQTHON**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])
