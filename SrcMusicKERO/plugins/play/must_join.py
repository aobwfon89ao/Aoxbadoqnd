from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from SrcMusicKERO import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/H_H_H_P":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("H_H_H_P", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/H_H_H_P".isalpha():
                link = "https://t.me/H_H_H_P"
            else:
                chat_info = await bot.get_chat("H_H_H_P")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n⌯︙قناة البوت: @H_H_H_P .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("𝙿𝚊𝚗𝚍𝚊 𝚂𝚘𝚞𝚛𝚌𝚎", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @H_H_H_P !")
