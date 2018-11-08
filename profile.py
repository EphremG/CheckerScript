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
url2 = 'http://192.168.6.2/profile.php?profile=Mg=='
r2 = s.get(url2)
#print r2.url
if 'Abeni' in str(r2.content):
	print('You have not fixed the vulnerable Yet! :(')
	exit(1)
else:
	print('Congratulations, You have Successfuly fixed the issue! :)')
	exit(0)
