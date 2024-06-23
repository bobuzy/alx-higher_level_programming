#!/usr/bin/python3
"""Module definition to lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    keyword = sys.argv[4]

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

    query = "SELECT cities.name \
             FROM cities INNER JOIN states ON states.id = cities.state_id \
             WHERE states.name = %(key)s"
    curr.execute(query, {'key': keyword})
    rows = curr.fetchall()

    temp = list(city[0] for city in rows)
    print(*temp, sep=", ")
    curr.close()
    db.close()
