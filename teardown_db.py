from databases.mysql import db_connector
from utils import config_util


def main():
    db_connection = db_connector.create_connection()
    db_name = config_util.get_value('mysql.database', 'name')

    # salesforce database teardown
    drop_query = f'DROP DATABASE IF EXISTS {db_name}'
    db_connector.execute_query(db_connection, drop_query)

    db_connection.close()


if __name__ == '__main__':
    main()
