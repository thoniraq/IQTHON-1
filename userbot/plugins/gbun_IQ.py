# @IQTHON C
import asyncio
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("تحذير الادمنيه"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "تحذير المستخدم من قبل الادمنيه...\n`"
    no_reason = "يحتمل انه ينشر اباحي"
    await event.edit("**استدعاء الادمنيه**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1094825801:
            await reply_message.reply("انتضر سيدي[klanrali](tg://user?id=1094825801) and ch @iqthon")
         else:
            jnl=("تحذير!! `"
                  "[{}](tg://user?id={})"
                  "` للادمن ...\n\n`"
                  "**اسم الشخص: ** __{}__\n"
                  "**ايدي الشخص : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**اسم مستخدم: ** `لايمتلك اسم مستخدم!`\n"
            elif usname != "None":
                jnl += "**اسم مستخدم** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**السبب: **"+gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "`تحذير المستخدم من قبل المسئولين. `"
        await event.reply(mention)
    await event.delete()
