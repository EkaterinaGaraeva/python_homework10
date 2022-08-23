import postgre as p

def delete_data_student(id, connection):
    # id = inf.menu_delete_student()
    delete_student = f"DELETE FROM students WHERE id = {id}"
    p.execute_query(connection, delete_student)

def delete_data_class(id, connection):
    # id = inf.menu_delete_class()
    delete_class = f"DELETE FROM classes WHERE id = {id}"
    p.execute_query(connection, delete_class)

