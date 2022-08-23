import postgre as p
import output as op

def change_data_student(new_student_data):
    student_id, *student_records = new_student_data
    student_records = tuple(student_records)
    update_students_data = (f"UPDATE students SET (surname, name, date_of_birth, class_id) = {student_records} WHERE id = {student_id}")
    p.execute_query(p.connection, update_students_data)

def change_data_class(new_class_data):
    class_id, *class_records = new_class_data
    class_records = tuple(class_records)
    update_classes_data = (f"UPDATE classes SET (number, letter) = {class_records} WHERE id = {class_id}")
    p.execute_query(p.connection, update_classes_data)

