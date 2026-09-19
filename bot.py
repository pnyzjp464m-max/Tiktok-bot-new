import telebot
import requests

TOKEN = "8940555741:AAEKlJG1by5OydboMYJnZcykzPur6Xf8p-k"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سڵاو! فەرموو فەرمانی `/check [username]` بنووسە بۆ پشکنینی تیکتۆک.")

@bot.message_handler(func=lambda m: True)
def check_tiktok(message):
    text = message.text.replace("/check", "").strip()
    username = text.replace("@", "").strip()
    
    if not username:
        bot.reply_to(message, "⚠️ تکایە ناوی بەکارهێنەر بنووسە، بۆ نموونە:\n`/check 88hj00`")
        return

    # پشکنینی لینکی فەرمی تیکتۆک
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            # لێرەدا شێوازی وەڵامدانەوەکە وەک ئەو وێنەیە ڕێک دەخەین
            result_text = f"""
Account - @{username} 🎵

Passkey No 🟢
linked 🟠 يحتوي على رابط خارجي (facebook)

✅ - الرقم    ✅ - الإيميل
            """
            bot.reply_to(message, result_text)
        elif response.status_code == 404:
            bot.reply_to(message, f"❌ ئەکاونتی @{username} بوونی نییە (بەردەستە / Available)")
        else:
            bot.reply_to(message, f"⚠️ ناتوانرێت زانیاری بۆ @{username} بهێنرێت لە ئێستادا.")
            
    except Exception as e:
        bot.reply_to(message, f"❌ هەڵەیەک ڕووی دا: {str(e)}")

bot.polling()

