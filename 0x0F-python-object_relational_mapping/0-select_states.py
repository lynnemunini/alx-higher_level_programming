#!/usr/bin/python3
"""
Module that has a scripts that lists all states from
the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """
    Execute only if the file is run directly
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
