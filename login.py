import requests
url = 'http://localhost/firstexercise/index.php'
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
else:
	print(' You have successfully solved the issue :) ')
