from MySQLdb import Connection
import MySQLdb


def create_connection():
    connection = None
    try:
        connection = MySQLdb.connector.connect(
            host="localhost",
            user="root",
            passwd="T#9758@qiph",
            database="province"
        )
        print("Connection to database was successful!")
    except any as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except any as e:
        print(f"The error '{e}' occurred")

connection =create_connection()
query = "SELECT * FROM your_table"
result = execute_query(connection, query)
for row in result:
    print(row)

connection.close()

