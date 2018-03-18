import requests
from bs4 import BeautifulSoup
records_arr = [] 
url_arr = []
status_code = []
with open("txt/UrlWithIn6Month-j-yanglv20180316142906.txt", "r", encoding = "utf-8") as f:
	with open("txt/records.txt", "w", encoding = "utf-8") as v: 
		with open("txt/title.txt", "w", encoding = "utf-8") as t:
			for i in f:
				url_arr.append(i.strip())
				try: 
					r = requests.get(i.strip())
					status_code.append(r.status_code)
					if r.status_code == 200:
						url_arr.append(i.strip())
						v.write(i.strip()+"\n")
						t.write(BeautifulSoup(r.title))
				except:
					print(i.strip())
print(status_code)

for i in url_arr:
	print (i)