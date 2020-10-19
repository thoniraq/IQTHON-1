"""
Syntax : .موقع <location name>
credits :@iqthon
"""

#help from @iqthon 

from geopy.geocoders import Nominatim
from userbot.utils import admin_cmd
from telethon.tl import types



@borg.on(admin_cmd(pattern="موقع ?(.*)"))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("ماذا يجب ان اجد ضع الامر بجانبه اسم مدينه او محافضه")

    await event.edit("finding")

    geolocator = Nominatim(user_agent="iqthon")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(
                    lat, lon
                )
            )
        )
        await event.delete()
    else:
        await event.edit("i coudn't find it")
        
        
