#!/usr/bin/python3
"""
Script to get all cities from  the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if (__name__ == '__main__'):

    args = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[0],
                           passwd=args[1], db=args[2], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities, "
                "states WHERE cities.state_id = states.id ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
