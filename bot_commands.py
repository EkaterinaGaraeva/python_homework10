from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, ConversationHandler
import datetime
from spy import *
import random

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/sum')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time().strftime("%H:%M:%S")}')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 456
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

# def echo(update, context):
#     msg='Hi, nice to see you!'
#     context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
#     update.message.reply_text(text=msg)

def UserMessage(update: Update, context: CallbackContext):
    if(update.message.text == "Кто ты?"):
        update.message.reply_text("Бот")
    else:
        try:
            update.message.reply_text(eval(update.message.text))
        except:
            update.message.reply_text("Не понятно")

candies = 2021
count = 0

def start_candy_game(update: Update, context: CallbackContext):
    n = random.randint(0, 1)
    global candies
    if n == 0:
        update.message.reply_text(f'Введите количество конфет: ')
        return 'game'
    elif n == 1:
        bot_move = (candies - 29) % 28
        update.message.reply_text(f'Ход бота: {bot_move}')
        candies -= bot_move
        update.message.reply_text(f'Осталось конфет: {candies}')
        update.message.reply_text(f'Введите количество конфет: ')
        return 'game'

def candy_game(update: Update, context: CallbackContext):
    player_move = update.message.text
    player_move = int(player_move)
    global candies
    candies -= player_move
    update.message.reply_text(f'Осталось конфет: {candies}')
    global count
    count += 1
    if candies == 0:
        update.message.reply_text(f'Выиграл игрок')
        return ConversationHandler.END
    if candies < 29:
        bot_move = candies
        update.message.reply_text(f'Ход бота: {bot_move}')
    elif player_move == 4 and count == 1:
        bot_move = 28
        update.message.reply_text(f'Ход бота: {bot_move}')
    elif player_move < 28:
        if (candies - 29) % 28 == 0:
            bot_move = 28 - player_move
            update.message.reply_text(f'Ход бота: {bot_move}')
        else:
            bot_move = (candies - 29) % 28
            update.message.reply_text(f'Ход бота: {bot_move}')
    elif player_move == 28:
        bot_move = 28
        update.message.reply_text(f'Ход бота: {bot_move}')
    candies -= bot_move
    update.message.reply_text(f'Осталось конфет: {candies}')
    if candies > 0:
        update.message.reply_text(f'Введите количество конфет: ')
        return 'game'
    else:
        update.message.reply_text(f'Выиграл бот')
        return ConversationHandler.END
    
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text(f'Игра завершена')
    return ConversationHandler.END

