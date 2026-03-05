from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from moderation import warn_user, mute_user
from antiflood import antiflood
from welcome import welcome_user

def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("warn", warn_user))
    app.add_handler(CommandHandler("mute", mute_user))

    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            welcome_user
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            antiflood
        )
    )

    print("Bot Running...")

    app.run_polling()


if __name__ == "__main__":
    main()
