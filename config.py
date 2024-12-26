from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("29376235"))
API_HASH = getenv("d7c10b0e14c1355dde0fec9d37c19b54")
BOT_TOKEN = getenv("7686693076:AAHNYZfoP0JdDnS8Ldy3XhLo1_uEjzmkuKc")
OWNER_ID = int(getenv("6517946837"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("SESSION")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tbcbotschat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tbc_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5090817443").split()))
FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
