from telegram.ext import Updater, CommandHandler
updater = Updater('TOKEN')

def sendlocation_method(bot , update):
    chat_id = update.message.chat_id
    bot.sendLocation(chat_id,'34.638226', '50.875897')

send_command= CommandHandler('sendlocation', sendlocation_method )
updater.dispatcher.add_handler(send_command)
updater.start_polling()

# for exit
updater.idle()
