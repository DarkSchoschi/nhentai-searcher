import random
import requests
from threading import Thread

print("Loading nHentai Searcher...")
url = "https://nhentai.net/"
print("nHentai has Status", requests.head(url).status_code)

codes = []

def start_searching():
	while True:
		for i in range(9):
			s = ""
			for k in range(6):
				j = random.randrange(10)
				s += str(j)
			codes.append(s)
		f = open('working.txt', 'w+')
		for code in codes:
			status = requests.head(url + "g/" + code).status_code
			if status == 301:
				print(str(code))
				f.write(str(code) + ", ")
		f.close()
		codes.clear()

thread = Thread(target = start_searching)
thread.start()
thread.join()
