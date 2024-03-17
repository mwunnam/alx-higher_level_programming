#!/usr/bin/python3
import MySQLdb


"""
A script which list all states fomr the database
"""


def list_states(username, passwd, database):
    """
    Function that list all the sate in the database
    usernama: The name of the user
    passwd: The password
    database: The name of the database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__"
