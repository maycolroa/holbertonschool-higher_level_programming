#!/usr/bin/python3
"""Wait, do you remember the previous task? Did you test """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""
                SELECT *
                FROM states
                WHERE name LIKE BINARY %s
                ORDER BY states.id""", (argv[4], ))
    query = cur.fetchall()
    for j in query:
        print(j)
    cur.close()
    db.close()
