#@iqthon 2021 c
import asyncio
from datetime import datetime
import io
import os
import requests
from telethon import events
from userbot.utils import progress, admin_cmd


@borg.on(admin_cmd("حذف خلفيه ?(.*)"))
async def _(event):
    HELP_STR = "قم برد على الصوره"
    if event.fwd_from:
        return
    if Config.REM_BG_API_KEY is None:
        await event.edit("يجب تعين ايبي فير من remove.bg هنا")
        return False
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
        reply_message = await event.get_reply_message()
      #@iqthon 2021 c
        await event.edit("تحليل الصوره")
        try:
            downloaded_file_name = await borg.download_media(
                reply_message,
                Config.TMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:
            await event.edit(str(e))
            return
        else:
            await event.edit("اقوم بالارسال الان")
            output_file_name = ReTrieveFile(downloaded_file_name)
            os.remove(downloaded_file_name)
    elif input_str:
        await event.edit("اقوم بالارسال الان")
        output_file_name = ReTrieveURL(input_str)
    else:
        await event.edit(HELP_STR)
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "BG_less.png"
            await borg.send_file(
                event.chat_id,
                remove_bg_image,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=message_id
            )
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit("تم ازاله خلقيه صوره في {} ثانيه, تابع @IQTHON".format(ms))
    else:
        await event.edit("ايبي الفير خطا. رجاء تعلم من @IQTHON\n`{}".format(output_file_name.content.decode("UTF-8")))


#@iqthon 2021 c
def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True
    )
    return r


def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    data = {
      "image_url": input_url
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        data=data,
        allow_redirects=True,
        stream=True
    )
    return r
