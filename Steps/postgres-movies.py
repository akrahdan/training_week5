import psycopg2

conn = psycopg2.connect(
    database="filmsdb",
    user="tester",
    host="localhost",
    port="5432",
    password="password"
)

cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE Movies (
       MOVIE_ID INT PRIMARY KEY,
       TITLE TEXT,
       GENRE TEXT,
       STUDIO TEXT,
       AUDIENCE_SCORE REAL,
       PROFIT REAL,
       ROTTEN_TOMATOES REAL,
       GROSS TEXT,
       YEAR INT);
 ''')
conn.commit()
conn.close()