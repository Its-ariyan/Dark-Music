import re

from pyrogram import Client, filters

from modules import *

from modules.config import API_ID, API_HASH

@Client.on_message((filters.regex(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}')) & filters.private)
async def on_clone(self, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)
    bot_token = bot_token[0] if bot_token else None
    bot_id = re.findall(r'\d[0-9]{8,10}', message.text)

    if not str(message.forward_from.id) != "93372553":
        msg = await message.reply_text(f"🔄 LOADING 🔄")
        try:
            ai = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "plugins"},
            )
            await ai.start()
            bot = await ai.get_me()
            details = {
                'bot_id': bot.id,
                'is_bot': True,
                'user_id': user_id,
                'name': bot.first_name,
                'token': bot_token,
                'username': bot.username
            }
            await msg.edit_text(f"Your Bot Has Been Successfully Started  @{bot.username}" ✅ \n\n Now Add Your Bot And Assistant @Cloner_Assistant To Your Chat!\n\nThanks for Cloning.")
        except BaseException as e:
            await msg.edit_text(f"⚠️ <b>BOT ERROR:</b>\n\n<code>{e}</code>\n\n❔ Forward this message to @Prince_ariyan_143 to be fixed.")
