#!/usr/bin/python3
"""Write a script that takes in the name of a state"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 INNER JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id", (argv[4], ))
    query = cur.fetchall()
    counter = 0
    for j in query:
        if counter != 0:
            print(", ", end="")
        print("%s" % j, end="")
        counter += 1
    print("")
    cur.close()
    db.close()
