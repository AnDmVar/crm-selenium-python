from constants import paths
from utils import file_util
from databases.mysql import db_connector


def main():
    db_connection = db_connector.create_connection()
    directory = paths.MYSQL_RESOURCES_DIR
    filename = 'init_salesforce_db.sql'

    # salesforce database setup
    init_db = file_util.read(directory, filename)
    db_connector.execute_operation(db_connection, init_db)

    db_connection.close()


if __name__ == '__main__':
    main()
