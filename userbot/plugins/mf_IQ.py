# @IQTHON AND DAV @KLANR C
import sys
from telethon import events, functions, __version__
from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="عراق"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""CH @IQTHON AND MY DAV @KLANR""")
