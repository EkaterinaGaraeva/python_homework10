import csv
import output as op
import postgre as p

def input_data_student(student_data):
    student_records = tuple(student_data)
    insert_query = (f"INSERT INTO students (surname, name, date_of_birth, class_id) VALUES {student_records}")
    p.connection.autocommit = True
    cursor = p.connection.cursor()
    cursor.execute(insert_query)

def input_data_class(class_data):
    class_records = tuple(class_data)
    insert_query = (f"INSERT INTO classes (number, letter) VALUES {class_records}")
    p.connection.autocommit = True
    cursor = p.connection.cursor()
    cursor.execute(insert_query)