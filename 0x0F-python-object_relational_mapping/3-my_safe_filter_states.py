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
    conn = MySQLdb.connect(host="localhost",
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
    cursor = conn.cursor()
    '''
    Take the cursor object and call the 'execute' function.
    The execute function requires one parameter, the query
    Escape query values by using the placholder %s method
    '''
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (user_input, ))

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
