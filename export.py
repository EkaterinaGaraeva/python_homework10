import csv
import output as op
import postgre as p

def export_csv_data_student():
    students = op.read_query_students()
    with open('student_base.csv', 'w', encoding='cp1251') as sb:
        file_writer = csv.writer(sb, delimiter=";", lineterminator="\r")
        file_writer.writerow(['student_id', 'surname', 'name', 'date_of_birth', 'class_id'])
        for student in students:
            student_id, surname, name, date_of_birth, class_id = student
            file_writer.writerow([str(student_id), surname, name, date_of_birth, class_id])

def export_csv_data_class():
    classes = op.read_query_classes()
    with open('class_base.csv', 'w', encoding='cp1251') as cb:
        file_writer = csv.writer(cb, delimiter=";", lineterminator="\r")
        file_writer.writerow(['class_id', 'number', 'letter'])
        for one_class in classes:
            class_id, number, letter = one_class
            file_writer.writerow([str(class_id), number, letter])

