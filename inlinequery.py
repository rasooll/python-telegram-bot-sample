from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
import logging
from uuid import uuid4
logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)

updater = Updater('TOKEN')

def start_method(bot, update):
    bot.sendMessage(update.message.chat_id, "Robot Started")

def inlinequery(bot, update):
    query = update.inline_query.query
    results = list()
    results.append(InlineQueryResultArticle(id = uuid4(), title="Uppercase", input_message_content=InputTextMessageContent(query.upper())))
    results.append(InlineQueryResultArticle(id = uuid4(), title="Lowercase", input_message_content=InputTextMessageContent(query.lower())))
    bot.answerInlineQuery(update.inline_query.id, results=results)

start_command = CommandHandler('start', start_method)
updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(InlineQueryHandler(inlinequery))
updater.start_polling()

# for exit
updater.idle()
