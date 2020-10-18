from telethon import events
from datetime import datetime


@command(pattern="^.بنك")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("البنك لديك!\n{} ch @iqthon".format(ms))
