import asyncio
from PyLyrics import *

@borg.on(slitu.admin_cmd(pattern="تحميل  (.*)"))
async def _(event):
    if event.fwd_from:
        return
    i = 0
    input_str = event.pattern_match.group(1)
    try:
        song = input_str.split("-")
        if len(song) == 1:
            await event.edit("الاستعمال:اكتب اسم المغني وبجانبه اسم الاغنيه")
        else:
            await event.edit("🔍︎جاري البحث")
            lyrics = PyLyrics.getLyrics(song[0].strip(), song[1].strip()).split("\n")
            lyric_message = f"Singing {song[0].strip()} from {song[1].strip()} 🎙"
            lyric_message += "\n\n" + "\n".join(lyrics)
            try:
                await event.edit(lyric_message)
            except:
                # TODO: send as file
                logger.info(lyric_message)
    except ValueError:
        await event.edit("لاتوجد")
