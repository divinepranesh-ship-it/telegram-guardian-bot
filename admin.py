from telegram.ext import ContextTypes
from telegram import Update

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.reply_to_message:

        user = update.message.reply_to_message.from_user.id
        chat = update.effective_chat.id

        await context.bot.ban_chat_member(chat, user)

        await update.message.reply_text("🚫 User banned")


async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.reply_to_message:

        user = update.message.reply_to_message.from_user.id
        chat = update.effective_chat.id

        await context.bot.restrict_chat_member(
            chat,
            user,
            permissions={}
        )

        await update.message.reply_text("🔇 User muted")
