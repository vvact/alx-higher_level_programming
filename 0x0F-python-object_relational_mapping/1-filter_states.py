#!/usr/bin/python3
"""
modules that lists all states with a name starting with N
from the database, connect with MySQLdb
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
 # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
