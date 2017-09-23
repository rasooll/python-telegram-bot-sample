from telegram.ext import Updater, CommandHandler
updater = Updater('TOKEN')

def start_method(bot, update):
    bot.sendMessage(update.message.chat_id, "Welcome to Our Bot. Developer : Ehsan Noreddini for Faranesh Course")
start_command = CommandHandler('start', start_method)
updater.dispatcher.add_handler(start_command)

updater.start_polling()
