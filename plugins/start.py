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
            ]
        ]
     ),
  ) 

@Client.on_message(command(["ping", "repo", "ariyan", "alive"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.delete()
    boottime = time.time()
    bot_uptime = escape_markdown(get_readable_time((time.time() - StartTime)))
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await message.reply_sticker("CAACAgQAAxkBAAICpGNPxPHPdw3hyH_5Rc1yGAGPH9htAAKOCQACpZdxUYvHGycIZ7mtKgQ")
    jay = await message.reply_photo(
        photo=f"{PING_IMG}",
        caption=" Pinging...⚡ ",
    )
    await jay.edit_text(
        f"""<b> ᴘᴏɴɢ ᴘɪɴɢ ! ⚡</b>\n  🏓 `{resp} ms`\n\n<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛsᴛs :</u></b>\n\n✨ ᴜᴘᴛɪᴍᴇ : {bot_uptime}\n🔮 ᴄᴘᴜ : {cpu}%\n💫 ᴅɪsᴋ : {disk}%\n❤️ ʀᴀᴍ : {mem}\n\n||ᴍᴀᴅᴇ 🖤 ʙʏ [ᴘʀɪɴᴄᴇ ᴀʀɪʏᴀɴ](https://t.me/Prince_ariyan_143)||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📨 sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📨 ᴜᴘᴅᴀᴛᴇ ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🔎 ʙᴏᴛ ʀᴇᴘᴏ ", url="https://github.com/Prince-ariyan-143/DarkxMusic"
                    )
                ]
            ]
        ),
    )
