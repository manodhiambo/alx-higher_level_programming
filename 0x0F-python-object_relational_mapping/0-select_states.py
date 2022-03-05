#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql username = argv[]
    mysql password = argv[]
    db_name = argv[]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT states.id, name FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
