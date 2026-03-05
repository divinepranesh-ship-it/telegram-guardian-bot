import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8783119872:AAEhWqeQi-WBeNMq3WexW7rP1HmvFXwABow"

logging.basicConfig(level=logging.INFO)

def start(update, context):
    update.message.reply_text("🛡 Spam Protection Bot Active")

def check_message(update, context):
    text = update.message.text.lower()

    spam_words = ["http", "t.me", "free money", "join channel"]

    for word in spam_words:
        if word in text:
            update.message.delete()
            update.message.reply_text("⚠️ Spam message removed")
            break

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, check_message))

    print("Bot started...")

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
