import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from random import choice
from modules.config import CLONER_TOKEN, ASSUSERNAME, BOT_NAME
from modules.config import API_ID, API_HASH
IMG = [
"https://te.legra.ph/file/60cd65b55a610aa57e3b6.jpg",
"https://te.legra.ph/file/5498ed073fcc4156480a5.jpg",
"https://te.legra.ph/file/c003017593aae380ed432.jpg",
"https://te.legra.ph/file/399981d0856d9d7a2ba7a.jpg",
"https://te.legra.ph/file/b1e8ba9ff892c8c71ab09.jpg",
"https://te.legra.ph/file/4d6cd1ef3d31de04bf63a.jpg",
"https://te.legra.ph/file/1087e8089a24ad301ea15.jpg",
"https://te.legra.ph/file/96c8384b61560f9ce38bb.jpg",
"https://te.legra.ph/file/e95bf98f6f650de9a307e.jpg",
"https://te.legra.ph/file/96dbf8412fe55751e9352.jpg",
"https://te.legra.ph/file/9533b87d747455d38a2e3.jpg",
"https://te.legra.ph/file/ce6decb1d20284e22b43c.jpg"
"https://te.legra.ph/file/db24a115ce2864b131d40.jpg",
"https://te.legra.ph/file/1aca448d82046ee746134.jpg",
]

MESSAGE = "Heya! I'm a music bot hoster/Cloner\n\nI can Host Your Bot On My Server within seconds\n\nTry /bash Token from @botfather"

@cloner.on_message(filters.private & filters.command("start"))
async def hello(client, message: Message):
    buttons = [
           [
                InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/ariyan_server"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/ariyan_discus"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, f"{choice(IMG)}", caption=MESSAGE, reply_markup=reply_markup)

##Copy from here 

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@cloner.on_message(filters.private & filters.command("bash"))
async def clone(bot, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /bash token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "plugins"})
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @{ASSUSERNAME} To Your Chat!\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!

