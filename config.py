import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("7335075593:AAG06tf2WDsGC33kY_Hu7q44trpkOfaBchs")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("26587447"))
API_HASH = getenv("a386dcee9212b536468e8205837181e7")
OWNER_NAME = getenv("Customer Service Match Bot")
ALIVE_NAME = getenv("MATCH BOT")
BOT_USERNAME = getenv("AutooreplyyBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AnnieAssistantHelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ElizaSupporters")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Updates_of_ElizaBot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/4104435ebaa2fdc591db1.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PereraSehath/Eliza-Annie-Video-Streamer")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/f529fa422259553b9a78f.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/89b7ca09f4b10e7ab117e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/b05b7f48a150177ac9d83.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/72cf9fc60847d67a7ee6a.jpg")
