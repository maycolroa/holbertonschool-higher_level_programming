#!/usr/bin/python3
"""Write a script that takes in an argument and displays"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    name = argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""".format(name))
    query = cur.fetchall()
    for j in query:
        if j[1] == name:
            print(j)
    cur.close()
    db.close()
