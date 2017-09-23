from telegram.ext import Updater, CommandHandler
updater = Updater('TOKEN')

def start_method(bot, update, args):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Welcome Dear " + str(args[0]) + str(args[1]))
start_command = CommandHandler('start', start_method,pass_args= True)
updater.dispatcher.add_handler(start_command)

updater.start_polling()

# for exit
updater.idle()
