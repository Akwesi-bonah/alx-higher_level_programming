#!/usr/bin/python3
"""List all states from the database passed as argument"""
import MySQLdb as Sql
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    dbName = sys.argv[3]
    arg = sys.argv[4]

    connector = Sql.connect(
        host="localhost",
        user=name,
        passwd=pwd,
        db=dbName,
        port=3306
    )

    sqlcmd = connector.cursor()
    sqlcmd.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(arg))

    rows = sqlcmd.fetchall()
    for row in rows:
        print(row)

    sqlcmd.close()
    connector.close()
