from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, ConversationHandler
import datetime
from spy import *
import random
import input as ip
import output as op
import delete as d
import change as ch
import postgre as p
import export as ex
import find as f

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


def menu(update: Update, context: CallbackContext):
    update.message.reply_text(f'Главное меню:\nУченики:\n/students\nКлассы:\n/classes\nВыход:\n/cancel')

def menu_students(update: Update, context: CallbackContext):
    update.message.reply_text(f'Ученики: \
                                \nДобавить ученика:\n/add_student \
                                \nУдалить ученика:\n/delete_student \
                                \nИзменить данные об ученике:\n/change_student \
                                \nПросмотреть все данные об учениках:\n/view_students_data \
                                \nЭкспорт в CSV:\n/export_students_csv \
                                \nПоиск ученика:\n/find_student \
                                \nГлавное меню:\n/menu \
                                \nВыход:\n/cancel')

def menu_classes(update: Update, context: CallbackContext):
    update.message.reply_text(f'Классы: \
                                \nДобавить класс:\n/add_class \
                                \nУдалить класс:\n/delete_class \
                                \nИзменить данные о классе:\n/change_class \
                                \nПросмотреть данные обо всех классах:\n/view_classes_data \
                                \nЭкспорт в CSV:\n/export_classes_csv \
                                \nГлавное меню:\n/menu \
                                \nВыход:\n/cancel')

def menu_input_student(update: Update, context: CallbackContext):
    update.message.reply_text(f'Введите данные об ученике')
    global student_data
    student_data = []
    update.message.reply_text(f'Фамилия ученика')
    return 'surname'

def input_surname(update: Update, context: CallbackContext):
    surname = update.message.text
    global student_data
    student_data.append(surname)
    update.message.reply_text(f'Имя ученика')
    return 'name'

def input_name(update: Update, context: CallbackContext):
    name = update.message.text
    global student_data
    student_data.append(name)
    update.message.reply_text(f'Дата рождения')
    return 'date_of_birth'

def input_date_of_birth(update: Update, context: CallbackContext):
    date_of_birth = update.message.text
    global student_data
    student_data.append(date_of_birth)
    # update.message.reply_text(f'Класс')
    text = f'Выберете id класса:\n{op.output_query_classes(op.read_query_classes())}'
    update.message.reply_text(text)
    return 'student_class'

def input_student_class(update: Update, context: CallbackContext):
    class_id = update.message.text
    global student_data
    student_data.append(class_id)
    update.message.reply_text(f'Данные ученика: \
                                \nФамилия: {student_data[0]} \
                                \nИмя: {student_data[1]} \
                                \nДата рождения: {student_data[2]} \
                                \nКласс: {student_data[3]} \
                                \nСохранить? Да/Нет')
    return 'save'

def save_student(update: Update, context: CallbackContext):
    ans = update.message.text
    if ans == 'Да':
        ip.input_data_student(student_data)
        update.message.reply_text(f'Данные сохранены')
        return ConversationHandler.END
    elif ans == 'Нет':
        return ConversationHandler.END

def menu_input_class(update: Update, context: CallbackContext):
    update.message.reply_text(f'Введите данные о классе')
    global class_data
    class_data = []
    update.message.reply_text(f'Цифра')
    return 'number'

def input_number(update: Update, context: CallbackContext):
    number = update.message.text
    global class_data
    class_data.append(number)
    update.message.reply_text(f'Буква')
    return 'letter'

def input_letter(update: Update, context: CallbackContext):
    letter = update.message.text
    global class_data
    class_data.append(letter)
    update.message.reply_text(f'Данные класса: \
                                \nКласс: {class_data[0]}{class_data[1]}\
                                \nСохранить? Да/Нет')
    return 'save'

def save_class(update: Update, context: CallbackContext):
    ans = update.message.text
    if ans == 'Да':
        ip.input_data_class(class_data)
        update.message.reply_text(f'Данные сохранены')
        return ConversationHandler.END
    elif ans == 'Нет':
        return ConversationHandler.END

def view_students_data(update: Update, context: CallbackContext):
    text = f'Данные об учениках:\n{op.output_query_students(op.read_query_students())}'
    update.message.reply_text(text)

def view_classes_data(update: Update, context: CallbackContext):
    text = f'Данные о классах:\n{op.output_query_classes(op.read_query_classes())}'
    update.message.reply_text(text)

def delete_student(update: Update, context: CallbackContext):
    text = f'Выберете id ученика\n{op.output_query_students(op.read_query_students())}'
    update.message.reply_text(text)
    return 'id_delete_student'

def id_delete_student(update: Update, context: CallbackContext):
    student_id = update.message.text
    d.delete_data_student(student_id, p.connection)
    update.message.reply_text(f'Ученик удален')
    return ConversationHandler.END

def delete_class(update: Update, context: CallbackContext):
    text = f'Выберете id класса\n{op.output_query_classes(op.read_query_classes())}'
    update.message.reply_text(text)
    return 'id_delete_class'

def id_delete_class(update: Update, context: CallbackContext):
    class_id = update.message.text
    d.delete_data_class(class_id, p.connection)
    update.message.reply_text(f'Класс удален')
    return ConversationHandler.END

def menu_change_student(update: Update, context: CallbackContext):
    update.message.reply_text(f'Выберете id ученика')
    text = f'{op.output_query_students(op.read_query_students())}'
    update.message.reply_text(text)
    return 'id_change_student'

def id_change_student(update: Update, context: CallbackContext):
    student_id = update.message.text
    global new_student_data
    new_student_data = []
    new_student_data.append(student_id)
    update.message.reply_text(f'Введите новые данные об ученике')
    update.message.reply_text(f'Фамилия ученика')
    return 'new_surname'

def input_new_surname(update: Update, context: CallbackContext):
    new_surname = update.message.text
    global new_student_data
    new_student_data.append(new_surname)
    update.message.reply_text(f'Имя ученика')
    return 'new_name'

def input_new_name(update: Update, context: CallbackContext):
    new_name = update.message.text
    global new_student_data
    new_student_data.append(new_name)
    update.message.reply_text(f'Дата рождения')
    return 'new_date_of_birth'

def input_new_date_of_birth(update: Update, context: CallbackContext):
    new_date_of_birth = update.message.text
    global new_student_data
    new_student_data.append(new_date_of_birth)
    # update.message.reply_text(f'Класс')
    text = f'Выберете id класса:\n{op.output_query_classes(op.read_query_classes())}'
    update.message.reply_text(text)
    return 'new_student_class'

def input_new_student_class(update: Update, context: CallbackContext):
    new_class_id = update.message.text
    global new_student_data
    new_student_data.append(new_class_id)
    update.message.reply_text(f'Новые данные ученика: \
                                \nФамилия: {new_student_data[0]} \
                                \nИмя: {new_student_data[1]} \
                                \nДата рождения: {new_student_data[2]} \
                                \nКласс: {new_student_data[3]} \
                                \nИзменить? Да/Нет')
    return 'change'

def change_student(update: Update, context: CallbackContext):
    ans = update.message.text
    if ans == 'Да':
        ch.change_data_student(new_student_data)
        update.message.reply_text(f'Данные изменены')
        return ConversationHandler.END
    elif ans == 'Нет':
        return ConversationHandler.END

def menu_change_class(update: Update, context: CallbackContext):
    update.message.reply_text(f'Выберете id класса')
    text = f'{op.output_query_classes(op.read_query_classes())}'
    update.message.reply_text(text)
    return 'id_change_class'

def id_change_class(update: Update, context: CallbackContext):
    class_id = update.message.text
    global new_class_data
    new_class_data = []
    new_class_data.append(class_id)
    update.message.reply_text(f'Введите новые данные о классе')
    update.message.reply_text(f'Цифра')
    return 'new_number'

def input_new_number(update: Update, context: CallbackContext):
    new_number = update.message.text
    global new_class_data
    new_class_data.append(new_number)
    update.message.reply_text(f'Буква')
    return 'new_letter'

def input_new_letter(update: Update, context: CallbackContext):
    new_letter = update.message.text
    global new_class_data
    new_class_data.append(new_letter)
    update.message.reply_text(f'Новые данные класса: \
                                    \nid: {new_class_data[0]} \
                                    \nКласс: {new_class_data[1]}{new_class_data[2]} \
                                    \nИзменить? Да/Нет')
    return 'change'

def change_class(update: Update, context: CallbackContext):
    ans = update.message.text
    if ans == 'Да':
        ch.change_data_class(new_class_data)
        update.message.reply_text(f'Данные изменены')
        return ConversationHandler.END
    elif ans == 'Нет':
        return ConversationHandler.END

def export_students_csv(update: Update, context: CallbackContext):
    ex.export_csv_data_student()
    update.message.reply_text(f'Данные экспортированы в CSV')

def export_classes_csv(update: Update, context: CallbackContext):
    ex.export_csv_data_class()
    update.message.reply_text(f'Данные экспортированы в CSV')

def find_student(update: Update, context: CallbackContext):
    update.message.reply_text(f'Введите фамилию ученика')
    return 'id_find_student'

def id_find_student(update: Update, context: CallbackContext):
    surname = update.message.text
    text = f.output_find_student(f.find_student(surname))
    update.message.reply_text(text)
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END

