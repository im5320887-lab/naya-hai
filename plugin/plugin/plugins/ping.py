from pyrogram import Client, filters

@Client.on_message(filters.command("ping"))
async def ping(_, message):
    await message.reply("🏓 Pong! Bot Alive.")
