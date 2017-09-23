from telegram.ext import Updater, CommandHandler
updater = Updater('TOKEN')

def start_method(bot, update, args):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, "TYPING")
    bot.sendMessage(chat_id, "Welcome Dear " + str(args[0]) + str(args[1]))

def sendphoto_method(bot, update):
    chat_id = update.message.chat_id
    photo = open('E:\mypic.jpg','rb')
    bot.sendPhoto(chat_id, photo, "test picture for telegram bot course")
    photo.close()
    
start_command = CommandHandler('start', start_method,pass_args= True)
photo_command = CommandHandler('sendphoto', sendphoto_method)
updater.dispatcher.add_handler(photo_command)
updater.dispatcher.add_handler(start_command)
updater.start_polling()

# for exit
updater.idle()
