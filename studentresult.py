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
url2 = 'http://192.168.6.2/result.php?rollid=2&class=1'
r2 = s.get(url2)
#print(r2.status_code)
if 'syntax error' in str(r2.content):
	print('1 You have not fixed the vulnerable Yet! :(')
	exit(1)
elif str(r2.content) == '':
	print('Content is empty :(')
	exit(1)
elif 'Abeni' not in str(r2.content) and str(r2.content) != '':
	print(' Congratulations, You have Successfully fixed the issue! :)')
	exit(0)
else:
	print('3You have not fixed the vulnerable Yet! :(')
	exit(1)
