#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd="",
                         db=sys.argv[2], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
