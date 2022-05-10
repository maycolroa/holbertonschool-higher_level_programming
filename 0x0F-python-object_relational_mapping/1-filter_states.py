#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states\
                WHERE name LIKE 'N%'\
                ORDER BY states.id")
    query = cur.fetchall()
    for i in query:
        if i[1][0] == 'N':
            print(i)
    cur.close()
    db.close()
