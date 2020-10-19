# @IQTHON AND DAV @KLANR C

from telethon import events, functions, types
from userbot.plugins.sql_helper.locks_sql import update_lock, is_locked, get_locks
from userbot.utils import admin_cmd


@borg.on(admin_cmd("قفل( (?P<target>\S+)|$)"))
async def _(event):
     # @IQTHON AND DAV @KLANR C
     # commands start with ".lock"
    if event.fwd_from:
        return
    input_str = event.pattern_match.group("target")
    peer_id = event.chat_id
    if input_str in (("بوتات", "تعليق", "ايميل", "توجيه", "رابط")):
        update_lock(peer_id, input_str, True)
        await event.edit(
            "Locked {}".format(input_str)
        )
    else:
        msg = None
        media = None
        sticker = None
        gif = None
        gamee = None
        ainline = None
        gpoll = None
        adduser = None
        cpin = None
        changeinfo = None
        if input_str:
            if "قفل الرسائل" in input_str:
                msg = True
            if "الوسائط" in input_str:
                media = True
            if "الملصقات" in input_str:
                sticker = True
            if "المتحركات" in input_str:
                gif = True
            if "الالعاب" in input_str:
                gamee = True
            if "الانلاين" in input_str:
                ainline = True
            if "gpoll" in input_str:
                gpoll = True
            if "الاضافه" in input_str:
                adduser = True
            if "التثبيت" in input_str:
                cpin = True
            if "المعلومات" in input_str:
                changeinfo = True
        banned_rights = types.ChatBannedRights(
            until_date=None,
            # view_messages=None,
            send_messages=msg,
            send_media=media,
            send_stickers=sticker,
            send_gifs=gif,
            send_games=gamee,
            send_inline=ainline,
            send_polls=gpoll,
            invite_users=adduser,
            pin_messages=cpin,
            change_info=changeinfo,
        )
        try:
            result = await borg(  # @IQTHON AND DAV @KLANR C
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=peer_id,
                    banned_rights=banned_rights
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(
                "تم القفل من صلاحيات المجموعه بنجاح"
            )


@borg.on(admin_cmd("فتح قفل ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    if input_str in (("بوتات", "تعليق", "ايميل", "توجيه", "رابط")):
        update_lock(peer_id, input_str, False)
        await event.edit(
            "UnLocked {}".format(input_str)
        )
    else:
        await event.edit(
            "تم فتح القفل بنجاح"
        )


@borg.on(admin_cmd("معلومات الاقفال"))
async def _(event):
    if event.fwd_from:
        return
    res = ""
    current_db_locks = get_locks(event.chat_id)
    if not current_db_locks:
        res = "لاتوجد اقفال من قبل حسابك شخصي في هل مجموعه"
    else:
        res = "🕷🇮🇶انت قافل من حسابك الشخصي: \n"
        res += "🕷🇮🇶 بوتات : `{}`\n".format(current_db_locks.bots)
        res += "🕷🇮🇶 تعليقات : `{}`\n".format(current_db_locks.commands)
        res += "🕷🇮🇶 ايميل : `{}`\n".format(current_db_locks.email)
        res += "🕷🇮🇶 توجيه : `{}`\n".format(current_db_locks.forward)
        res += "🕷🇮🇶 روابط : `{}`\n".format(current_db_locks.url)
    current_chat = await event.get_chat()
    try:
        current_api_locks = current_chat.default_banned_rights
    except AttributeError as e:
        logger.info(str(e))
    else:
        res += "🕷🇮🇶صلاحيات المجموعه للارسال: \n"
        res += "🕷🇮🇶 الرسائل : `{}`\n".format(current_api_locks.send_messages)
        res += "🕷🇮🇶 ميديا : `{}`\n".format(current_api_locks.send_media)
        res += "🕷🇮🇶 ملصقات: `{}`\n".format(current_api_locks.send_stickers)
        res += "🕷🇮🇶 متحركات : `{}`\n".format(current_api_locks.send_gifs)
        res += "🕷🇮🇶 العاب : `{}`\n".format(current_api_locks.send_games)
        res += "🕷🇮🇶 الانلاين : `{}`\n".format(current_api_locks.send_inline)
        res += "🕷🇮🇶 الجميع : `{}`\n".format(current_api_locks.send_polls)
        res += "🕷🇮🇶 اضافه : `{}`\n".format(current_api_locks.invite_users)
        res += "🕷🇮🇶 التثبيت : `{}`\n".format(current_api_locks.pin_messages)
        res += "🕷🇮🇶 معلومات : `{}`\n".format(current_api_locks.change_info)
    await event.edit(res)


@borg.on(events.MessageEdited())  # pylint:disable=E0602
@borg.on(events.NewMessage())  # pylint:disable=E0602
async def check_incoming_messages(event):
    # @IQTHON AND DAV @KLANR C
    peer_id = event.chat_id
    if is_locked(peer_id, "تعليق"):
        entities = event.message.entities
        is_command = False
        if entities:
            for entity in entities:
                if isinstance(entity, types.MessageEntityBotCommand):
                    is_command = True
        if is_command:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "لايمكنني ليس لدي اذن ادمن هنا. \n`{}`".format(str(e))
                )
                update_lock(peer_id, "تعليق", False)
    if is_locked(peer_id, "توجيه"):
        if event.fwd_from:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "لايمكنني ليس لدي اذن ادمن هنا. \n`{}`".format(str(e))
                )
                update_lock(peer_id, "توجيه", False)
    if is_locked(peer_id, "ايميل"):
        entities = event.message.entities
        is_email = False
        if entities:
            for entity in entities:
                if isinstance(entity, types.MessageEntityEmail):
                    is_email = True
        if is_email:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "ليس لدي اذن ادمن هنا. \n`{}`".format(str(e))
                )
                update_lock(peer_id, "ايميل", False)
    if is_locked(peer_id, "رابط"):
        entities = event.message.entities
        is_url = False
        if entities:
            for entity in entities:
                if isinstance(entity, (types.MessageEntityTextUrl, types.MessageEntityUrl)):
                    is_url = True
        if is_url:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "ليس لدي ادمن هنا. \n`{}`".format(str(e))
                )
                update_lock(peer_id, "رابط", False)


@borg.on(events.ChatAction())  # # @IQTHON AND DAV @KLANR C
async def _(event):
    # # @IQTHON AND DAV @KLANR C
    # # @IQTHON AND DAV @KLANR C
    if is_locked(event.chat_id, "بوتات"):
        # bots are limited Telegram accounts,
        # and cannot join by themselves
        if event.user_added:
            users_added_by = event.action_message.from_id
            is_ban_able = False
            rights = types.ChatBannedRights(
                until_date=None,
                view_messages=True
            )
            added_users = event.action_message.action.users
            for user_id in added_users:
                user_obj = await borg.get_entity(user_id)
                if user_obj.bot:
                    is_ban_able = True
                    try:
                        await borg(functions.channels.EditBannedRequest(
                            event.chat_id,
                            user_obj,
                            rights
                        ))
                    except Exception as e:
                        await event.reply(
                            "ليس لدي اذن ادمن هنا. \n`{}`".format(str(e))
                        )
                        update_lock(event.chat_id, "بوتات", False)
                        break
            if Config.G_BAN_LOGGER_GROUP is not None and is_ban_able:
                ban_reason_msg = await event.reply(
                    "!البوتات [user](tg://user?id={}) الرجاء عدم اضافه بوتات هنا.".format(users_added_by)
                )
