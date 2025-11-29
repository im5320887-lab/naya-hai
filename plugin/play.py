from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from pytgcalls.types.input_stream import AudioPiped
from main import call

@Client.on_message(filters.command("play"))
async def play(_, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("❌ Use: /play song name")

    result = YoutubeSearch(query, max_results=1).to_dict()
    link = f"https://youtube.com{result[0]['url_suffix']}"

    chat_id = message.chat.id
    await message.reply(f"🎧 Playing **{query}**\n🔗 {link}")

    try:
        await call.join_group_call(
            chat_id,
            AudioPiped(link),
        )
    except:
        await call.change_stream(
            chat_id,
            AudioPiped(link),
        )
