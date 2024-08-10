import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from SrcMusicKERO import app

#استارت
@app.on_message(
    filters.command(["الاوامر"],""))
async def italy(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/29f784eb49d230ab62e9e.mp4",
        caption=f"""✅ **𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚖𝚢 𝚍𝚎𝚊𝚛** {message.from_user.mention}
     

❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰▰
 𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌 𝚂𝚘𝚞𝚛𝚌𝚎
𝚃𝚘 𝚍𝚒𝚜𝚙𝚕𝚊𝚢 𝚝𝚑𝚎 𝚖𝚎𝚖𝚋𝚎𝚛𝚜 𝚔𝚎𝚢𝚋𝚘𝚊𝚛𝚍
»»»»»»  /VIP  «««««« .
么 ← 𝙶𝚛𝚘𝚞𝚙 𝚘𝚛𝚍𝚎𝚛𝚜 .
么 ← 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚘𝚛𝚍𝚎𝚛𝚜 .
么 ← 𝙱𝚘𝚝 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 .
么 ← 𝚂𝚘𝚞𝚛𝚌𝚎 𝚏𝚎𝚊𝚝𝚞𝚛𝚎𝚜 .
▰▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "✧مـجـمـوعـات✧", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "❅قـنـوات❅", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "❅✧𝚋𝚘𝚝✧❅", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "◁ 𝚜𝚘𝚞𝚛𝚌𝚎 ▷", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر المجموعه
@app.on_callback_query(filters.regex("italygro"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر المجموعات ♬**
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰

么 ← لتشغيل اغنيه اكتب : تشغيل او شغل
么 ← لتشغيل فيديو اكتب : فيديو 
么 ← لأنهاء الاغنيه اكتب : ايقاف او انهاء 
么 ←لتخطي الاغنيه اكتب : تخطي .**
么 ←اذا حدث خطأ او اعادة التشغيل اكتب 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅:** /restart .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "❅✧𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜❅✧", callback_data=f"italycha"),
                    InlineKeyboardButton(
                        "✧❅𝚋𝚘𝚝❅✧", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "✧❅𝚜𝚘𝚞𝚛𝚌𝚎❅✧", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر القناه
@app.on_callback_query(filters.regex("italycha"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜 ♬**
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰
么 ←لتشغيل اغنيه اكتب : تشغيل او شغل 
么 ←لتشغيل فيديو اكتب : فيديو 
么 ← لأنهاء الاغنيه اكتب : ايقاف او انهاء 
么 ← لتخطي الاغنيه اكتب : تخطي 
么 ←اذا حدث خطأ او اعادة التشغيل اكتب 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅:** /restart .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "✧❅𝚃𝚑𝚎 𝚐𝚛𝚘𝚞𝚙𝚜❅✧", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "❅✧𝚋𝚘𝚝✧❅", callback_data=f"italybot"),
                ],[
                InlineKeyboardButton(
                        "❅✧𝚜𝚘𝚞𝚛𝚌𝚎✧❅", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر البوت
@app.on_callback_query(filters.regex("italybot"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر 𝚋𝚘𝚝 ♬**
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰

么عمل اذاعه في البوت قم برد علي الاذاعه واكتب : اذاعه 
么عرض احصائيات البوت اكتب : الاحصائيات 
么عرض سرعه البوت اكتب : بينج 
么للتحكم في لغه البوت اكتب : اللغه 
么للتحكم في وضع التشغيل اكتب : الاعدادات 
么اوامر الحظر والرفع في كيبورد المطور 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "❅✧𝚃𝚑𝚎 𝚐𝚛𝚘𝚞𝚙𝚜✧❅", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "✧❅𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜❅✧", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "❅✧𝚜𝚘𝚞𝚛𝚌𝚎✧❅", callback_data=f"italysou"),
                ],[
                    InlineKeyboardButton(
                        "𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر مميزات 𝚜𝚘𝚞𝚛𝚌𝚎
@app.on_callback_query(filters.regex("italysou"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر سورس الحيتان ♬**
   المس الامر لنسخ والاستخدام
❅─────✧❅✦❅✧─────❅
▰▰▰▰▰▰▰▰▰▰▰▰
- لعرض كليشه 𝚜𝚘𝚞𝚛𝚌𝚎 اكتب : سورس .
- لعرض مين في الكول اليك الامر  : مين في الكول .
- لزخرفه عربي او انجلش اكتب  : فه واسم الزخرفه مثال زخرفه hossam . .
- لعرض بوت الحذف اكتب   : بوت حذف .
- لعمل كت او تويت اليك الامر  : كت او تويت .
- لعرض مطور البوت اكتب : المطور .
- لعرض اسم البوت اكتب : بوت .
- لعرض الايدي الخاص بك في الجروب او البرايفت اكتب : ا او ايدي .
- لصناعة رابط تليجراف ارسل الصوره برد عليه : تليجراف .
- لعرض لينك الجروب ارسل : لينك او رابط .
- لطباعة صوره علي التريمنال ارسل الرساله انجليزي برد عليه : طباعه .
- لترجمة نص مثال : /tr ar nour
- لتحويل ملصق الي صورة قم برد علي الملصق : pict .
- لتحويل الصوره الي ملصق قم برد علي الملصق : stik .
- لعرض كود الملصق قم برد علي الملصق : code .
- لعرض اسمك اكتب : اسمي .
- لمعرفة معلومات شخص قم برد عليه : كشف .
- لعمل تاك للاعضاء استخدم امر : تاك .
**- لايقاف تاك للاعضاء استخدم امر
 الاغنيه اكتب : تخطي .**
么 ←اذا حدث خطأ او اعادة التشغيل اكتب 
▰▰▰▰▰▰▰▰▰▰▰▰
❅─────✧❅✦❅✧─────❅:** `/cancel` .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "𝚃𝚑𝚎 𝚐𝚛𝚘𝚞𝚙𝚜❅", callback_data=f"italygro"),
                    InlineKeyboardButton(
                        "𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜✧", callback_data=f"italycha"),
                ],[
                InlineKeyboardButton(
                        "𝚋𝚘𝚝", callback_data=f"italybot"),
                ],[
                    InlineKeyboardButton(
                        "𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك المطورين
@app.on_callback_query(filters.regex("italydev"))
async def ayamr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""
[♡]𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚐𝚛𝚘𝚞𝚙 𝚏𝚘𝚛 𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛𝚜 @H_H_H_P
[♡]𝙲𝚑𝚊𝚗𝚗𝚎𝚕 @R_Q_R7
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛", url=f"https://t.me/L_Y_Y_Y"), 
                    InlineKeyboardButton("𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝", url=f"https://t.me/AT_W2"),
                ],[               
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
