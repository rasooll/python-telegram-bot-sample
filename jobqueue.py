from telegram.ext import Updater, CommandHandler, Job
updater = Updater('TOKEN')
jobqueue = updater.job_queue

def myFirstJob_Method(bot, update):
    bot.sendMessage('@[YOUR CHANNEL ID]','Job Executed :)')

myFirstJob = Job(myFirstJob_Method, 10.0)
jobqueue.put(myFirstJob,next_t=0.0)

updater.start_polling()

# for exit
updater.idle()
