import psycopg2
from datetime import datetime

connection = psycopg2.connect(
    database="Team3DB",
    user="Team3",
    password="3Team3",
    host='127.0.0.1',
    port='5432'
)
cursor = connection.cursor()
# cursor.execute("INSERT INTO Weather (temp,day) VALUES  (%s, %s)",(90,datetime.now()))
# connection.commit()
cursor.execute('SELECT * FROM Weather')
z = cursor.fetchone()
print(z[2])
cursor.close()
connection.close()
