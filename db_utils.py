import mysql.connector
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')

def connect_to_database():
    host = config.get('DB', 'host')
    user = config.get('DB', 'user')
    password = config.get('DB', 'password1')
    database = config.get('DB', 'database')

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def query_database(query, params=None):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

def get_exam_info(exam_identifier):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        query = "SELECT * FROM m_exam WHERE exam_name = %s"
        cursor.execute(query, (exam_identifier,))
        subject_info = cursor.fetchone()

        if subject_info:
            print("Exam Information:")
            for index, field in enumerate(subject_info):
                print(f"Field {index + 1}: {field}")
        else:
            print("Exam not found with identifier:", exam_identifier)

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"An error occurred while retrieving subject information: {e}")
