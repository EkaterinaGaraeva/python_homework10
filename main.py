from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, ConversationHandler, MessageHandler
from bot_commands import *
from spy import *
import random

updater = Updater('5519017312:AAF8439QGRpAYun39XwvNNCSSMeDRyLg5sM')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))

updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('candy', start_candy_game)],
                                                    states={
                                                        'game': [MessageHandler(Filters.text, candy_game)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))


print('server start')
updater.start_polling()
updater.idle()
