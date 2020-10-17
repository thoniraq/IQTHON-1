# @iqthon c 2021
"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "تهكير":

        await event.edit(input_str)

        animation_chars = [
        
           "خكرر خكر..`",
            "تل ابيب....",
            "جاري تهكير العدو بنسبه: ... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
            "جاري تهكير العدو بنسبه: ... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "جاري تهكير العدو بنسبه: ... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",    
            "جاري تهكير العدو بنسبه: ... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "جاري تهكير العدو بنسبه: ... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "جاري تهكير العدو بنسبه: ... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "جاري تهكير العدو بنسبه: ... 84%\n█████████████████████▒▒▒▒ ",
            "جاري تهكير العدو بنسبه: ... 100%\n█████████████████████████ ",
            "تم تهكير العدو بنجاح تل ابيب تنجح..."
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])

