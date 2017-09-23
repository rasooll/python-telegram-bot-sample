from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
updater = Updater('TOKEN')

def ReplyKeyboard_Test(bot, update):
    my_list = [['First ITEM', 'Second ITEM']]
    bot.sendMessage(update.message.chat_id, "Please Select something: ", reply_markup=ReplyKeyboardMarkup(my_list))

send_command= CommandHandler('start', ReplyKeyboard_Test )
updater.dispatcher.add_handler(send_command)
updater.start_polling()

# for exit
updater.idle()
