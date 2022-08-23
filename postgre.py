import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # connection.commit()
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    # finally:
    #     if connection:
    #         cursor.close()
    #         connection.close()
    #         print("Соединение с PostgreSQL закрыто")


# connection = create_connection(
#     "postgres", "postgres", "1111", "127.0.0.1", "5432"
# )

# create_database_query = "CREATE DATABASE students"
# create_database(connection, create_database_query)

connection = create_connection(
    "students", "postgres", "1111", "127.0.0.1", "5432"
)

create_students_table = """
CREATE TABLE IF NOT EXISTS students (
  id SERIAL PRIMARY KEY,
  surname TEXT NOT NULL,
  name TEXT NOT NULL, 
  date_of_birth DATE,
  class_id INTEGER REFERENCES students(id)
)
"""

execute_query(connection, create_students_table)

create_classes_table = """
CREATE TABLE IF NOT EXISTS classes (
  id SERIAL PRIMARY KEY, 
  number INTEGER, 
  letter TEXT NOT NULL
)
"""

execute_query(connection, create_classes_table)