#!/usr/bin/python3
"""
This is a script to list all the cites in the table
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
            INNER JOINT state ON states.id=cities.state_id""")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
