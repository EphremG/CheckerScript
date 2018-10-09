import requests

url = 'http://localhost/thesis/index.php'
values = {
	'login': 'letmein',
	'username': 'student',
	'password': '123',
	'role' : 'admin'
}

r = requests.post(url, data=values)
print(r.url)
#print r.content

if 'student.php' in r.url:
	print('Congratulations, You have Successfuly fixed the issue! :)')
else:
	print('You have not fixed the vulnerable Yet! :(')
