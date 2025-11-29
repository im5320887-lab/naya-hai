from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, SESSION

bot = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client(SESSION, api_id=API_ID, api_hash=API_HASH)

call = PyTgCalls(user)

import os
for file in os.listdir("./plugins"):
    if file.endswith(".py"):
        __import__(f"plugins.{file[:-3]}")

bot.start()
user.start()
call.start()

print("🔥 Telegram VideoCall Music Bot Active!")
bot.idle()
