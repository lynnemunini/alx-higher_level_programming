#!/usr/bin/python3

"""
Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """
    Execute only if the file is run directly
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd="", db=sys.argv[2])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \
            'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
