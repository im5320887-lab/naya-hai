from pyrogram import Client, filters
from main import call

@Client.on_message(filters.command("stop"))
async def stop(_, message):
    chat_id = message.chat.id
    try:
        await call.leave_group_call(chat_id)
        await message.reply("🛑 Stopped!")
    except:
        await message.reply("⚠️ Bot is not in VC")
