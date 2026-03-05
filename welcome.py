async def welcome_user(update, context):

    for member in update.message.new_chat_members:

        await update.message.reply_text(
            f"Welcome {member.first_name} 🎉"
        )
