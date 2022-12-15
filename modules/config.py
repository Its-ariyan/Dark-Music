import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18634285"))
API_HASH = getenv("API_HASH", "f6daa5619fa9d5e10d1f52efa10b39b1")
ASSUSERNAME = getenv("ASSUSERNAME")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME", "AriyanXMusicBot")
BOT_TOKEN = getenv("BOT_TOKEN", "5752836942:AAGulHxkDn7EPkKo9-rgJIzoLqdkvCcp1Tw")
CLONER_TOKEN = getenv("CLONER_TOKEN")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Prince_ariyan_143")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQBaqPLLtCPjlfG3sf80Xn3IkTui0MDNuTR_PplZ6lmqN2IFjmWveowue3BQc7jMVvpCckxD1_EjyOyJnT4Td6lgvxVMaT8PsTyp9niwkLiIhwFyeLCD61CFk_AFjEW80qRJ7lGR5LCz80eZGldI-xeEfLr0lIXBne-x4oNdyE8Vt2gslDg5hHPbz6_GVnSG2Y9gdlR_1xLhjv64ZLWns-l4K2mLWbG_rV-oifeUT5iBHqKAqbJ-ooD4k5A753rBMxOj3M5R4UrFRasXB6HAhab8H9Usb-7DitoBTuLIZP3Gv-2CRx3uLFyOPR17_6xWR2F0_V9P54o9wa-hrAlYgV2FAAAAAVYkY5sA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5787575060").split()))
aiohttpsession = aiohttp.ClientSession()
