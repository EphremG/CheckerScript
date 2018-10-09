import requests
s = requests.Session()
url = 'http://localhost/final/index.php'
values = {
	'login': 'letmein',
	'username': 'student',
	'password': 'student',
	'role' : 'student'
}

r = s.post(url, data=values)
print(r.url)
url2 = 'http://localhost/final/result.php?rollid=2&class=1'
r2 = s.get(url2)
print r2.url
if 'strong>Oh snap! Invalid Roll Id' in r2.content:
	print('success')
else:
	print('vulnerable')
