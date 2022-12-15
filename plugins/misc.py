import os
import asyncio
import requests
import aiohttp
import yt_dlp
from pyrogram.types import Message
from pyrogram import Client, filters
from modules.helpers.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from modules.helpers.decorators import authorized_users_only
from modules.clientbot.clientbot import client as user
from modules.config import BOT_USERNAME, STRING_SESSION as SESSION_NAME
from modules.helpers.get_file_id import get_file_id
from youtube_search import YoutubeSearch

# ×=======================> ᴜsᴇʀʙᴏᴛ ᴊᴏɪɴ ᴄᴏᴍᴍᴀɴᴅ <==================================× #


@Client.on_message(
    command(["join", " userbotjoin"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "» ᴀssɪsᴛᴀɴᴛ sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ.​")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, "» ᴀssɪsᴛᴀɴᴛ ᴀʟʀᴇᴀᴅʏ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ.​")
        return await user.send_message(chat_id, "» ᴀssɪsᴛᴀɴᴛ ᴀʟʀᴇᴀᴅʏ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ.​")



# ×=======================> ɪɴғᴏ <==================================× #

@Client.on_message(command(["id", "stickerid", f"id@{BOT_USERNAME}"]))
async def showid(_, message: Message):
    await message.delete()
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>ᴄʜᴀᴛ ɪᴅ</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>ᴜsᴇʀ ɪᴅ</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
