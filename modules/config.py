import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18634285"))
API_HASH = getenv("API_HASH", "f6daa5619fa9d5e10d1f52efa10b39b1")
BOT_NAME = getenv("BOT_NAME", "Sanki Music")
BOT_USERNAME = getenv("BOT_USERNAME", "SankiXMusicBot")
BOT_ID = int(getenv("BOT_ID", "5482381188"))
BOT_TOKEN = getenv("BOT_TOKEN", "5482381188:AAHUm_YKT0C-F81t_bIH_FpVgaUGKErK71s")
OWNER_ID = getenv("OWNER_ID", "5761513990")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ariyan_discus")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ariyan104:ariyan104@cluster0.1iptuzv.mongodb.net/?retryWrites=true&w=majority")
STRING_SESSION = getenv("STRING_SESSION", "BQCz_3O0ESIeW8d6uEWOQcfrG1aOXEC6CZ2HxwLICiBN8FI6Myll35qIMvK43sr_7tGdg0HA12Ba-HNovkEgzr6c4eEKbsOANWL0AaQJg3bnijc9PiR2COglnffx4RlWzZX1RIPsiHH8gXS-Yg9Kte0uyfSrPgw09KJxJSmcRXoghFL0GE4O8W3NRxutrduSCgAaTy17KkoqGTCQDSY-vvUlw52bzhL2rn4BXm5oxxJDwaDl8UAU9S1uQFPB84ECXMntraWqK9wyJ73uEg8NHVglwjdu2UUUswRA12tULluiNn_vcGp3xpxcoKKFiSfwaav7_4WAYuZ8cjyxzacktIcrAAAAAUYNJBMA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5761513990").split()))
IMG_1 = "https://telegra.ph/file/3505f3c0abf6008b3f6b9.jpg"
aiohttpsession = aiohttp.ClientSession()
