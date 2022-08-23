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

updater.dispatcher.add_handler(CommandHandler('menu', menu))
updater.dispatcher.add_handler(CommandHandler('students', menu_students))
updater.dispatcher.add_handler(CommandHandler('classes', menu_classes))
updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('add_student', menu_input_student)],
                                                    states={
                                                        'surname': [MessageHandler(Filters.text, input_surname)],
                                                        'name': [MessageHandler(Filters.text, input_name)],
                                                        'date_of_birth': [MessageHandler(Filters.text, input_date_of_birth)],
                                                        'student_class': [MessageHandler(Filters.text, input_student_class)],
                                                        'save': [MessageHandler(Filters.text, save_student)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))
updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('add_class', menu_input_class)],
                                                    states={
                                                        'number': [MessageHandler(Filters.text, input_number)],
                                                        'letter': [MessageHandler(Filters.text, input_letter)],
                                                        'save': [MessageHandler(Filters.text, save_class)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))
updater.dispatcher.add_handler(CommandHandler('view_students_data', view_students_data))
updater.dispatcher.add_handler(CommandHandler('view_classes_data', view_classes_data))
updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('delete_student', delete_student)],
                                                    states={
                                                        'id_delete_student': [MessageHandler(Filters.text, id_delete_student)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))
updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('delete_class', delete_class)],
                                                    states={
                                                        'id_delete_class': [MessageHandler(Filters.text, id_delete_class)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))
updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('change_student', menu_change_student)],
                                                    states={
                                                        'id_change_student': [MessageHandler(Filters.text, id_change_student)],
                                                        'new_surname': [MessageHandler(Filters.text, input_new_surname)],
                                                        'new_name': [MessageHandler(Filters.text, input_new_name)],
                                                        'new_date_of_birth': [MessageHandler(Filters.text, input_new_date_of_birth)],
                                                        'new_student_class': [MessageHandler(Filters.text, input_new_student_class)],
                                                        'change': [MessageHandler(Filters.text, change_student)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))
updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('change_class', menu_change_class)],
                                                    states={
                                                        'id_change_class': [MessageHandler(Filters.text, id_change_class)],
                                                        'new_number': [MessageHandler(Filters.text, input_new_number)],
                                                        'new_letter': [MessageHandler(Filters.text, input_new_letter)],
                                                        'change': [MessageHandler(Filters.text, change_class)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))
updater.dispatcher.add_handler(CommandHandler('export_students_csv', export_students_csv))
updater.dispatcher.add_handler(CommandHandler('export_classes_csv', export_classes_csv))
updater.dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('find_student', find_student)],
                                                    states={
                                                        'id_find_student': [MessageHandler(Filters.text, id_find_student)]
                                                        },
                                                    fallbacks=[CommandHandler('cancel', cancel)]))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel))


print('server start')
updater.start_polling()
updater.idle()
