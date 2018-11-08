import requests
url = 'http://192.168.6.2/loginexercise/index.php'
values = {
	'login': 'letmein',
	'username': 'student',
	'password': 'student',
	'role' : 'admin'
}
r = requests.post(url, data=values)
print(r.url)
#print r.content
if 'admin.php' in r.url:
	print('The issue is not solved yet! :( ')
	exit(1)
else:
	print(' You have successfully solved the issue :) ')
	exit(0)
