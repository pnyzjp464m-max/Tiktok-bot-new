import telebot
import requests

TOKEN = "8940555741:AAEKlJG1by5OydboMYJnZcykzPur6Xf8p-k"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سڵاو! فەرموو ناوی بەکارهێنەری تیکتۆک بنووسە بۆ پشکنینی دروست:")

@bot.message_handler(func=lambda m: True)
def check_tiktok(message):
    text = message.text.replace("/check", "").strip()
    username = text.replace("@", "").strip()
    
    if not username:
        bot.reply_to(message, "⚠️ تکایە ناوی بەکارهێنەری تیکتۆک بنووسە!")
        return

    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers)
        
        # پشکنینی ڕاستەقینەی بوونی ئەکاونتەکە
        if response.status_code == 200:
            bot.reply_to(message, f"🔍 پشکنین بۆ: @{username}\n\n✅ **ئەکاونتەکە بوونی هەیە (Active)**\n🔗 لینک: {url}")
        elif response.status_code == 404:
            bot.reply_to(message, f"🔍 پشکنین بۆ: @{username}\n\n❌ **ئەکاونتی نەدۆزرایەوە (بەردەستە / Available)**")
        else:
            bot.reply_to(message, f"⚠️ ناتوانرێت داتای @{username} لە ئێستادا بەدەستبهێنرێت.")
            
    except Exception as e:
        bot.reply_to(message, f"❌ هەڵەیەک ڕووی دا: {str(e)}")

bot.polling()
