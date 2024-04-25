from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/3ed5104dca0afa25e7c98.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/3ed5104dca0afa25e7c98.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/honey_suppoort")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Honey_networks")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://graph.org/file/3ed5104dca0afa25e7c98.jpg"
