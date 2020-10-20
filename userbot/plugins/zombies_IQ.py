#"""@iqthon iraq ©

"""Cmd= `.المحذوفين`
Usage: Searches for deleted accounts in a groups and channels.
Use .المحذوفين تنظيف to remove deleted accounts from the groups and channels.
\nPorted by ©[klanr](t.me/klanr) and ©[iraqthon](t.me/tele_thon)"""

from telethon import events
from userbot.utils import admin_cmd
#
from asyncio import sleep
from os import remove

from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.types import (ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto)


# =================== CONSTANT ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================



@borg.on(admin_cmd(pattern=f"المحذوفين", allow_sudo=True))
@borg.on(events.NewMessage(pattern="^.المحذوفين(?: |$)(.*)", outgoing=True))
async def rm_deletedacc(show):
    """ For .zombies command, list all the ghost/deleted/zombie accounts in a chat. """

    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**⌔︙ عزيزي لاتوجد حسابات محذوفه ⛔️**"

    if con != "clean":
        await show.edit("**⌔︙ جـاري البـحث على حسابات محذوفـه  ♻️**")
        async for user in show.client.iter_participants(show.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"**⌔︙ لقـد وجدت 🔄 {del_u}** امـا في حاله اردت مسح المحذوفين قم بارسا`.المحذوفين clean` ⚠️**"
      await show.edit(del_status)
        return
    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit("**⌔︙ عزيزي انا لست ادمن هنا ⚠️**")
        return

    await show.edit("**⌔︙ يمكنني حذف الحسابات محذوفه من مجموعتك ♻️**")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.edit("**⌔︙لايمكنني ليس لدي صلاحيه حظر 🚫**")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1


    if del_u > 0:
        del_status = f"**تم الازالـه ♻️ {del_u} حسابات المحذوفه 🚫**"

    if del_a > 0:
        del_status = f"**تم الازالـه ♻️ {del_u} حسابات المحذوفه 🚫 \
        \n {del_a} لايمكني حذف الادمنيه ⚠️**"


    await show.edit(del_status)
    await sleep(2)
    await show.delete()


    if Config.G_BAN_LOGGER_GROUP is not None:
        await show.client.send_message(
            Config.G_BAN_LOGGER_GROUP, "#CLEANUP\n"
            f"تنظيف **{del_u}** حسابات المحذوفه 🚫 !!\
            \nالمحادثه: {show.chat.title}(`{show.chat_id}`)")
