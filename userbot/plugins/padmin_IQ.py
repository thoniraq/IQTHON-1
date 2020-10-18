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
            "**(1) تمت صلاحيه: ✅**",
            "**(2) ارسال وسائط: ☑️**",
            "**(2) تمت الوسائط: ✅**",
            "**(3) ارسال ملصقات: ☑️**",
            "**(3) تمت ملصقات: ✅**",    
            "**(4) ارسال استطلاع: ☑️**",
            "**(4) تمت استطلاع: ✅**",
            "**(5) ارسال روابط: ☑️**",
            "**(5) تمت روابط: ✅**",
            "**(6) اضافه اعضاء: ☑️**",
            "**(6) تمت اضافه: ✅**",
            "**(7) تثبيت رسائل: ☑️**",
            "**(7) تمت التثبيت: ✅**",
            "**(8)معلومات مجموعه: ☑️**",
            "**(8) تم وصول معلومات مجموعه: ✅**",
            "**تم منح الاذن بنجاح**",
            "**تابع قناتنا @IQTHON**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])
