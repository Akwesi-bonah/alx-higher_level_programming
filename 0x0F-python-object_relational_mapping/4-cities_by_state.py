#!/usr/bin/python3
"""List all cites from the database passed as argument"""
import MySQLdb as Sql
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    dbName = sys.argv[3]

    connector = Sql.connect(
        host="localhost",
        user=name,
        passwd=pwd,
        db=dbName,
        port=3306
    )

    sqlcmd = connector.cursor()
    sqlcmd.execute("""
    SELECT c.id, c.name, s.name
    FROM cities AS c INNER JOIN
    states AS s ON s.id=c.state_id 
    """)

    rows = sqlcmd.fetchall()
    for row in rows:
        print(row)

    sqlcmd.close()
    connector.close()
