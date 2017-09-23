from telegram.ext import Updater, CommandHandler
from telegram.error import BadRequest
import logging
updater = Updater('TOKEN')

logging.basicConfig(filename='mylogs.txt',format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)
def startMethod(bot, update):
    bot.sendMessage(update.message.chat_id, 'a'*40960)

def callback_errorhandler(bot, update, error):
    try:
        raise error
    except BadRequest:
        print "Bad Request"
        logging.getLogger().info("Bad Request")
        bot.sendMessage(update.message.chat_id, "Bad Request")
send_command= CommandHandler('start', startMethod )
updater.dispatcher.add_handler(send_command)
updater.dispatcher.add_error_handler(callback_errorhandler)
updater.start_polling()

# for exit
updater.idle()
