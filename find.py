import csv
import postgre as p
import psycopg2
from psycopg2 import OperationalError
import output as op

def find_student(surname):
    select_students = f"SELECT * FROM students WHERE surname = '{surname}'"
    students = op.execute_read_query(p.connection, select_students)
    return students

def output_find_student(students):
    text = ''
    for student in students:
        student_id, surname, name, date_of_birth, class_id = student
        text += f'id: {student_id}; Фамилия: {surname}; Имя: {name}; Дата рождения: {date_of_birth}; Класс: {class_id}\n'
    return text

