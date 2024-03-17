#!/usr/bin/python3
import MySQLdb
import sys

"""
A script which list all states fomr the database
"""

if __name__ == "__main__":
    def list_states(username, passwd, database):
        """
        Function that list all the sate in the database
        usernama: The name of the user
        passwd: The password
        database: The name of the database
        """
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()
