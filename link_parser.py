import requests, sys

base_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
ending = str(sys.argv[1])

while True:
	link = base_url + ending
	content = requests.get(link).text
	if content.startswith('We'):
		print(content)
		break
	else:
		ending = content