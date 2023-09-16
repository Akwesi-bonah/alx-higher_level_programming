#!/usr/bin/python3
"""List all cites from the database passed as argument"""
import MySQLdb as Sql
import sys

if __name__ == "__main__":
    name = "Admin"
    pwd = "1122"
    dbName = "alx_db"
    arg = "Texas" # sys.argv[4]

    connector = Sql.connect(
        host="localhost",
        user=name,
        passwd=pwd,
        db=dbName,
        port=3306
    )

    sqlcmd = connector.cursor()
    sqlcmd.execute("""
    SELECT  c.name FROM cities AS c
    INNER JOIN states AS s ON s.id=c.state_id
    WHERE s.name=%s
    """, (arg,))

    rows = sqlcmd.fetchall()
    lst = [row[0] for row in rows]

    print(*lst, sep=", ")

    sqlcmd.close()
    connector.close()
