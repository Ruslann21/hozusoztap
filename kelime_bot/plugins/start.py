from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

START = """
**🔮 Merhaba, Harika Logolar Oluşturmak İçin Beni Kullanabilirsiniz...**

➤ Tıklayınız /help Veya Beni Nasıl Kullanacağınızı Bilmek İçin Aşağıdaki Düğmeye basın
"""

HELP = """
**🖼 Beni Kullanmak için?**

**Oyun oynamak Yapmak için -** `/game yazınız`
**Oyunu kapamak için - ** `/son yazınız`
**♻️ Örnek:** 
`/game`
`/son`
"""

# Komut
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://i.ibb.co/khRz42f/Turkish-Voice.jpg",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Grubumuz 💬", url="https://t.me/GonulkahvesiTr")]]))

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://i.ibb.co/khRz42f/Turkish-Voice.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Kanal 📣", url="https://t.me/Botdestekgrubu")]]))


# Mahoaga Ufak çaplı düzenlemeler.
@Client.on_message(filters.command("game")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun Zaten Grubunuzda Devam Ediyor ✍🏻 \n Oyunu durdurmak için yazıp /stop durdurabilirsiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tarafından! \nKelime Bulma Oyunu Başladı .\n\nİyi Şanslar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Kazandığınız Puan: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluk : {int(len(kelime_list)/2)} 

✏️ Karışık harflerden doğru kelimeyi bulun
        """
        await c.send_message(m.chat.id, text)
        
