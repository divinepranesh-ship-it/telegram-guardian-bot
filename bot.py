import asyncio
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import config
import filters as msgfilter
import admin

logging.basicConfig(level=logging.INFO)

async def start(update, context):
    await update.message.reply_text("🛡 Guardian Bot Active")

async def message_handler(update, context):
    if update.message.text:
        await msgfilter.check_message(update, context)

async def main():

    app = ApplicationBuilder().token(config.TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ban", admin.ban))
    app.add_handler(CommandHandler("mute", admin.mute))

    app.add_handler(
        MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler)
    )

    print("Guardian bot running...")

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
