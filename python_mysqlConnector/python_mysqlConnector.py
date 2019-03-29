
import mysql.connector


mydb = mysql.connector.connect(
  host="xxx",
  user="xxxx",
  passwd="xxxx",
  database="xxxx"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
