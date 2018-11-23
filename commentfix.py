import mysql.connector
import requests

connection = mysql.connector.connect(
  host="192.168.6.2",
  user="root",
  passwd="rootroot",
  database="srms"
)

sql= """delete from comment where 1"""
mycursor = connection.cursor()
mycursor.execute(sql)
connection.commit()

sql= """INSERT INTO comment (id, studentId, comment, Name) VALUES (1, 1, 'Student1 Comment', 'Ephrem'), (2, 2, 'Student2 Comment', 'Abeni')"""
mycursor = connection.cursor()
mycursor.execute(sql)
connection.commit()
print(mycursor.rowcount, "record inserted.")

s = requests.Session()
url = 'http://192.168.6.2/index.php'
values = {
	'login': 'letmein',
	'username': 'ephrem',
	'password': 'ephrem',
	'role' : 'student'
}

r = s.post(url, data=values)
url = 'http://192.168.6.2/deletecomment.php?commentid=2'

url = s.get(url)
if 'syntax error' in str(r2.content):
	print('1 You have not fixed the vulnerable Yet! :(')
	exit(1)
elif str(r2.content) == '':
	print('2You have not fixed the vulnerable Yet! :(')
	exit(1)
elif 'ABENI' in str(url.content):
	print('Congratulations, You have Successfuly fixed the issue! :)')
	exit (0)
else:
	print('You have not fixed the vulnerable Yet! :(')
	exit (1)
