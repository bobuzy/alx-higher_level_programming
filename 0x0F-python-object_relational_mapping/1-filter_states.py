#!/usr/bin/python3
"""Module definition to lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
    except MySQLdb.ERROR as error:
        print("Error connecting to database: {}".format(error))
        sys.exit(1)

    curr = db.cursor()

    curr.execute("SELECT * FROM states WHERE name \
                 LIKE BINARY 'N%' ORDER BY id ASC")
    rows = curr.fetchall()

    for row in rows:
        print(row)
    curr.close()
    db.close()
