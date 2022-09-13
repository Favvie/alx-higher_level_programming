#!/usr/bin/python3
"""the module of life"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')

    for x in cursor:
        print(x)
