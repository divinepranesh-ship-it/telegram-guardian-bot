from telegram import ChatPermissions

async def warn_user(update, context):

    if update.message.reply_to_message:

        await update.message.reply_text("⚠ Warning issued")


async def mute_user(update, context):

    if update.message.reply_to_message:

        user = update.message.reply_to_message.from_user.id

        await context.bot.restrict_chat_member(
            update.message.chat_id,
            user,
            permissions=ChatPermissions(
                can_send_messages=False
            )
        )
