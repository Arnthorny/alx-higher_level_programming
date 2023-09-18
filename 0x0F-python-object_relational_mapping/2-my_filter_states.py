#!/usr/bin/python3
"""
Script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


if (__name__ == '__main__'):

    args = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[0],
                           passwd=args[1], db=args[2], charset="utf8")

    cur = conn.cursor()
    query = ('SELECT * FROM states WHERE name'
             ' LIKE "{}" ORDER BY id ASC'.format(args[3]))
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
