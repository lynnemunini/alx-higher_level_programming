#!/usr/bin/python3

"""
Script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd="",
                         db=sys.argv[2], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON\
            state_id = states.id WHERE states.name=%s\
            ORDER BY cities.id", (sys.argv[3], ))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        if i + 1 == len(rows):
            print(row[1])
        print(row[1], end=", ")
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
