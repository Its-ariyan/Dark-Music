import asyncio
import random
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton




DARK_IMG = (
"https://telegra.ph//file/0879fbdb307005c1fa8ab.jpg",
"https://telegra.ph//file/19e3a9d5c0985702497fb.jpg",
"https://telegra.ph//file/b5fa277081dddbddd0b12.jpg",
"https://telegra.ph//file/96e96245fe1afb82d0398.jpg",
"https://telegra.ph//file/fb140807129a3ccb60164.jpg",
"https://telegra.ph//file/09c9ea0e2660efae6f62a.jpg",
"https://telegra.ph//file/3b59b15e1914b4fa18b71.jpg",
"https://telegra.ph//file/efb26cc17eef6fe82d910.jpg",
"https://telegra.ph//file/ab4925a050e07b00f63c5.jpg",
"https://telegra.ph//file/d169a77fd52b46e421414.jpg",
"https://telegra.ph//file/dab9fc41f214f9cded1bb.jpg",
"https://telegra.ph//file/e05d6e4faff7497c5ae56.jpg",
"https://telegra.ph//file/1e54f0fff666dd53da66f.jpg",
"https://telegra.ph//file/18e98c60b253d4d926f5f.jpg",
"https://telegra.ph//file/b1f7d9702f8ea590b2e0c.jpg",
"https://telegra.ph//file/7bb62c8a0f399f6ee1f33.jpg",
"https://telegra.ph//file/dd00c759805082830b6b6.jpg",
"https://telegra.ph//file/3b996e3241cf93d102adc.jpg",
"https://telegra.ph//file/610cc4522c7d0f69e1eb8.jpg",
"https://telegra.ph//file/bc97b1e9bbe6d6db36984.jpg",
"https://telegra.ph//file/2ddf3521636d4b17df6dd.jpg",
"https://telegra.ph//file/72e4414f618111ea90a57.jpg",
"https://telegra.ph//file/a958417dcd966d341bfe2.jpg",
"https://telegra.ph//file/0afd9c2f70c6328a1e53a.jpg",
"https://telegra.ph//file/82ff887aad046c3bcc9a3.jpg",
"https://telegra.ph//file/8ba64d5506c23acb67ff4.jpg",
"https://telegra.ph//file/8ba64d5506c23acb67ff4.jpg",
"https://telegra.ph//file/a7cba6e78bb63e1b4aefb.jpg",
"https://telegra.ph//file/f8ba75bdbb9931cbc8229.jpg",
"https://telegra.ph//file/07bb5f805178ec24871d3.jpg",
)

PM_HOME = """**ʜᴇʟʟᴏ {},
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜꜱɪᴄ ʙᴏᴛ**.
‣ **ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ**.
‣ **ɪ ʜᴀᴠᴇ ᴀʟᴍᴏꜱᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ɴᴇᴇᴅꜱ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ**
‣ **ᴛʜɪꜱ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ. ꜱᴏ ɪᴛ'ꜱ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʀᴇ ꜱᴛᴀʙɪʟɪᴛʏ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ʙᴏᴛꜱ**!
‣ **ɪ ᴄᴀɴ ᴅᴏ ᴏᴛʜᴇʀ ᴛʜɪɴɢꜱ ʟɪᴋᴇ ᴘɪɴꜱ ᴇᴛᴄꜱ**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️**"""


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(DARK_IMG),
        caption=(f"{PM_HOME}"),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🥀 sᴜᴘᴘᴏʀᴛ", url="https://t.me/ariyan_discus"),
            InlineKeyboardButton("🏡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/ariyan_server")
        ],
        [
            InlineKeyboardButton("🔥 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs 🔥", callback_data="help_cmd")
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive", "/repo"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        random.choice(DARK_IMG),
        caption=f"""ʏᴏᴜ ᴋɴᴏᴡ ɪ ᴀᴍ ғᴀsᴛ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs. """,
        reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="🥀 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/ariyan_discus"),
                InlineKeyboardButton(text="🏡 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/ariyan_server"),
            ],
            [
                InlineKeyboardButton(text="ᴄʟᴏsᴇ 📌", callback_data="close_play"),
           ],
        ]
     ),
  ) 
