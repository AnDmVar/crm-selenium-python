from utils import config_util
import mysql.connector.cursor
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        # host, port, username, password
        connection_params = config_util.get_values('mysql')
        connection = mysql.connector.connect(**connection_params)
        print('MySQL server connection successful')
    except Error as err:
        print(f'Error: "{err}"')

    return connection


def use(connection):
    cursor = connection.cursor()
    try:
        db_name = config_util.get_value('mysql.database', 'name')
        cursor.execute(f'USE {db_name}')
        print('Use successful')
    except Error as err:
        print(f'Error: "{err}"')
    finally:
        cursor.close()


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query successful')
    except Error as err:
        print(f'Error: "{err}"')
    finally:
        cursor.close()


def execute_operation(connection, operation):
    cursor = connection.cursor(buffered=True)
    try:
        for result in cursor.execute(operation, multi=True):
            if result.with_rows:
                result.fetchall()
        connection.commit()
        print('Operation successful')
    except Error as err:
        print(f'Error: "{err}"')
    finally:
        cursor.close()


def read_query(connection, query, dictionary=False):
    cursor = connection.cursor(dictionary=dictionary)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print('Query successful')
        return result
    except Error as err:
        print(f'Error: "{err}"')
    finally:
        cursor.close()
