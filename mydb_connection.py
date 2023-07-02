from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def mydb_connection():
    """Connect to MYSQL database"""

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MYSQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established')
        else:
            print('Connection failed')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed')


if __name__=='__main__':
    mydb_connection()
