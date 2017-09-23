from telegram.ext import Updater, CommandHandler
import logging
updater = Updater('TOKEN')
logging.basicConfig(filename='mylogs.txt', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)
def start_method(bot, update):
    bot.sendMessage(update.message.chat_id, "Test MSG")

my_command = CommandHandler('start', start_method)
updater.dispatcher.add_handler(my_command)


updater.start_polling()

# for exit
updater.idle()
