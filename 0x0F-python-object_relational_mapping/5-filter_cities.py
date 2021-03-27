#!/usr/bin/python3
'''
Script that lists all cities from the database hbtn_0e_4_usa
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    try:
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
        working environments through the same connection to the
        database
        '''
        cursor = conn.cursor()
        '''
        Take the cursor object and call the 'execute' function.
        The execute function requires one parameter, the query
        Escape query values by using the placholder %s method
        '''
        query = """SELECT cities.name
        FROM cities
        LEFT JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s"""
        cursor.execute(query, (state,))
        query_rows = cursor.fetchall()
        for i in range(len(query_rows)):
            print(query_rows[i][0], end="")
            if query_rows[i + 1] is not None:
                print(', ', end="")
        cursor.close()
        conn.close()

    except:
        pass

    print()
