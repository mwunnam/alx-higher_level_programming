#!/usr/bin/python3
import sys
import MySQLdb
"""
This script list only states starting with N
"""

if __name__ == "__main__":
    db = db.connect(host="localhost", port=3366, user=sys.argv[1],
                    passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE state_name LIKE 'N%' ORDER BY
                   state.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
