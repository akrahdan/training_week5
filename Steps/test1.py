import psycopg2

connection = psycopg2.connect(
    database="testdb",
    host="localhost",
    user="tester",
    password="password",
    port="5432"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM SALES LIMIT 10;")
print(cursor.fetchall())
connection.commit()
connection.close()

