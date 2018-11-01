import requests
s = requests.Session()
url = 'http://192.168.6.2/index.php'
values = {
	'login': 'letmein',
	'username': 'ephrem',
	'password': 'ephrem',
	'role' : 'student'
}

r = s.post(url, data=values)
#print(r.url)
url2 = 'http://localhost/ctf/result.php?rollid=2&class=1'
r2 = s.get(url2)
#print r2.url
if 'Abeni' in r2.content:
	print('You have not fixed the vulnerable Yet! :(')
else:
	print('Congratulations, You have Successfuly fixed the issue! :)')

