#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa

One that is safe from SQL injections
"""
import sys
import MySQLdb


if (__name__ == '__main__'):

    args = sys.argv[1:]

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[0],
                           passwd=args[1], db=args[2], charset="utf8")

    cur = conn.cursor()
    query = ("SELECT name FROM cities WHERE cities.state_id IN "
             "(SELECT id FROM states WHERE name = %s)")
    params = (args[3], )
    cur.execute(query, params)
    query_rows = cur.fetchall()

    l_query_rows = list(map(lambda x: x[0], query_rows))
    print(*l_query_rows, sep=', ')
    cur.close()
    conn.close()
