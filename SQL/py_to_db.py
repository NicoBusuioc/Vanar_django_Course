### BASICS DB to python functionality ###
import psycopg2

# create a connection
conn = psycopg2.connect("dbname=mini_social_ddd user=postgres password=qazwsx")
cursor = conn.cursor()

# execute an opereration
# cursor.execute("INSERT INTO users VALUES(5, 'psyco', 'p@e.d', '454646');")
# conn.commit()

cursor.execute("SELECT * FROM users;")
res = cursor.fetchall()
for item in res:
    print(item)