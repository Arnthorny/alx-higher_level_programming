#!/usr/bin/python3
"""
Script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if (__name__ == '__main__'):

    args = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[0],
                           passwd=args[1], db=args[2], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE REGEXP_LIKE(name, '^N', 'c') "
                "ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
