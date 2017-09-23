from telegram.ext import Updater, CommandHandler
updater = Updater('TOKEN')

def senddocument_method(bot , update):
    chat_id = update.message.chat_id
    document= open('E:\document.chm', 'rb')
    bot.sendDocument(chat_id, document,'document_id_123123123', 'test document for python telegram bot course')

send_command= CommandHandler('senddocument', senddocument_method )
updater.dispatcher.add_handler(send_command)
updater.start_polling()

# for exit
updater.idle()
