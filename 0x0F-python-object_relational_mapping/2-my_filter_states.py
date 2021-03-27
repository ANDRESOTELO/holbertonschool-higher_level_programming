#!/usr/bin/python3
'''
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    database = argv[3]
    user_input = argv[4]

    '''
    Connecting to a MySQL database.
    This is the function that is used to connect to the database,
    in our case MySQL
    '''
    data_base = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=user_name,
                                passwd=password,
                                db=database,
                                charset="utf8")
    '''
    The cursor object is an abstraction specified in the Python
    DB-API 2.0. It gives us the ability to have multiple seperate
    working environments through the same connection to the database
    '''
    cursor = data_base.cursor()
    '''
    Take the cursor object and call the 'execute' function.
    The execute function requires one parameter, the query.
    '''
    query = "SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC"
    cursor.execute(query.format(user_input))
    '''
    After you execute any SELECT statement, you will need to
    use one of these methods to obtain your results.
    Method 1: Fetch All-at-Once
    '''
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    data_base.close()
