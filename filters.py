import time
from telegram import ChatPermissions
import config

user_messages = {}
warnings = {}

async def warn_user(update, context):

    user = update.effective_user.id
    chat = update.effective_chat.id

    if user not in warnings:
        warnings[user] = 0

    warnings[user] += 1

    if warnings[user] >= config.MAX_WARNINGS:

        await context.bot.restrict_chat_member(
            chat,
            user,
            permissions=ChatPermissions(can_send_messages=False)
        )

        await context.bot.send_message(
            chat,
            "🚫 User muted for repeated violations."
        )

    else:

        await context.bot.send_message(
            chat,
            f"⚠️ Warning {warnings[user]}/{config.MAX_WARNINGS}"
        )


async def check_message(update, context):

    user = update.effective_user.id
    chat = update.effective_chat.id
    text = update.message.text.lower()

    now = time.time()

    if user not in user_messages:
        user_messages[user] = []

    user_messages[user].append(now)

    user_messages[user] = [
        t for t in user_messages[user]
        if now - t < config.TIME_WINDOW
    ]

    if len(user_messages[user]) > config.SPAM_LIMIT:
        await update.message.delete()
        await warn_user(update, context)
        return True

    if config.BLOCK_LINKS:
        if any(link in text for link in config.BLOCKED_LINKS):
            await update.message.delete()
            await warn_user(update, context)
            return True

    if any(word in text for word in config.BAD_WORDS):
        await update.message.delete()
        await warn_user(update, context)
        return True

    return False
