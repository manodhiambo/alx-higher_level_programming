#!/usr/bin/python3
# script that lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[]
    password = argv[]
    db_name = argv[]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT states.id, name FROM states WHERE name "
                "COLLATE latin1_general_cs "
                "LIKE 'N%' "
                "ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
