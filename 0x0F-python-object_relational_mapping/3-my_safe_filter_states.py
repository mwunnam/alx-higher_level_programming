#!/usr/bin/python3
"""
This script list only states starting with N
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    text = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE '%s'", (text, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
