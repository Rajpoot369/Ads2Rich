import telebot

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to AdRich - Watch Ads & Earn! Click the link below to start earning:

https://yourwebsite.com")

bot.polling()
