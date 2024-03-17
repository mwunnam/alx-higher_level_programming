#!/usr/bin/python3
import sys
import MySQLdb
"""
This script list only states starting with N
"""

if __name__ == "__main__":
    db = db.connect(host="localhost", port=3306, user=sys.argv[1],
                    passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY
                   states.id ASC")
    for row in rows:
        print(row)

    cursor.close()
    db.close()
