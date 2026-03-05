import time
from collections import defaultdict
from config import SPAM_LIMIT, TIME_WINDOW

messages = defaultdict(list)

async def antiflood(update, context):

    user = update.message.from_user.id
    chat = update.message.chat_id

    now = time.time()

    messages[user].append(now)

    messages[user] = [
        t for t in messages[user] if now - t < TIME_WINDOW
    ]

    if len(messages[user]) > SPAM_LIMIT:

        await update.message.delete()

        await context.bot.ban_chat_member(chat, user)
