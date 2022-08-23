import csv
import input as ip
import postgre as p
import psycopg2
from psycopg2 import OperationalError

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def read_query_students():
    select_students = "SELECT * FROM students"
    students = execute_read_query(p.connection, select_students)
    return students

def output_query_students(students):
    text = ''
    for student in students:
        student_id, surname, name, date_of_birth, class_id = student
        text += f'id: {student_id}; Фамилия: {surname}; Имя: {name}; Дата рождения: {date_of_birth}; Класс: {class_id}\n'
    return text

def read_query_classes():
    select_classes = "SELECT * FROM classes"
    classes = execute_read_query(p.connection, select_classes)
    return classes

def output_query_classes(classes):
    text = ''
    for one_class in classes:
        class_id, number, letter = one_class
        text += f'id: {class_id}; Класс: {number}{letter}\n'
    return text

