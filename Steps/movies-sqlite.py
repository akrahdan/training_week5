import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()
# movie = ('The Harder They Fall', 'Thomas', 2017)
# cursor.execute('''
#   INSERT INTO movies VALUES (?, ?, ?)
#  ''', movie)


#  cursor.execute('''
#   INSERT INTO movies VALUES ('Money Heist', 'Dzidula', 2019)
#  ''')



cursor.execute("SELECT * from movies")

print(cursor.fetchall())

connection.commit()

connection.close()