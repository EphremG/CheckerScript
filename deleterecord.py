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
i = 1
while i< 100:
	url2 = 'http://192.168.6.2/deletecomment.php?commentid='+str(i)
	i+=1
	print url2
	r2 = s.get(url2)

