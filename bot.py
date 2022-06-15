import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler


telegram_bot_token = "5426860615:AAEU0qFZbcAzPmN9HxXHJm7012CBkfoIv1g"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher
URL="https://api.shasta.trongrid.io/v1/accounts/TSaJqQ1AZ2bEYyqBwBmJqCBSPv8KPRTAdv/transactions"


def start(update, context):
    chat_id = update.effective_chat.id
    message=URL
    
    
    
    context.bot.send_message(chat_id=chat_id, text=message)
dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()