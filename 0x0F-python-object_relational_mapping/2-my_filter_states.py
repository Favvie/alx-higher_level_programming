#!/usr/bin/python3
""" a module"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE name="{:s}" ORDER BY id'
                   .format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
