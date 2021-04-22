# pylint: disable=E1101
import psycopg2
import getpass
from configparser import ConfigParser

def read_config_file(filename,section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db_data = {}
    params = parser.items(section)
    for param in params:
        db_data[param[0]] = param[1]

    return db_data

def connect_to_database(**params):
    try:
        connection = psycopg2.connect(**params)
        
        cursor = connection.cursor()
        print('PostgreSQL database version: ')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connecton closed')

if __name__ == '__main__':

    params = read_config_file('database.cfg')

    password = getpass.getpass('Enter password: ')
    params['password'] = password

    connect_to_database(**params)
