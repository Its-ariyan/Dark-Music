import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18634285"))
API_HASH = getenv("API_HASH", "f6daa5619fa9d5e10d1f52efa10b39b1")
ASSUSERNAME = getenv("ASSUSERNAME", "Cloner_Assistant")
BOT_NAME = getenv("BOT_NAME", "Sanki Music")
BOT_USERNAME = getenv("BOT_USERNAME", "SankiXMusicBot")
BOT_TOKEN = getenv("BOT_TOKEN", "5814817311:AAFgDeNnJ3YQ0aOviXzH23bKDB94aBiHuaU")
CLONER_TOKEN = getenv("CLONER_TOKEN", "5757128136:AAHbXOr22S1LNZteuoPNrJY1RNq_bL9yKpg")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Prince_ariyan_143")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQB30YXSZQ-bUnJ3t58pQq9xcvEn00HldElVxMBlyWEFi8K6s0uTm1LnsB_O57VUL16vN1wjGmg-4WNGMHohvv3gdw0dnq5Ly3mTCa17Wf6F6A_bQe5urOFp2pzxK9E7P6aaPXivmhoUutJ9-5hWGMxjhiW0sA-7NpRmk7YcisqiV9WgFzLcNR4idIUZFn3oHGK_JVl8mf3QKitoZOxtPBxL-2vdKt12ey1vxt9JyyWnmTSVZdOez0-WvHhv0NVfDTkcolk0ExtYKTiw3MFoP3jxJAUeXdHxKkePOyxSdfpXEnxwh86YzxBeOZNy_RTeNBtiriU2EYUfxjl3Z-0L72O2AAAAAS0QGFEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5787575060").split()))
aiohttpsession = aiohttp.ClientSession()
