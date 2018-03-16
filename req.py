import requests
url_arr = []
url_valid = []
with open("UrlWithIn6Month-j-yanglv20180315123848.txt", "r", encoding = "utf-8") as f:
	for i in f:
		url_arr.append(i.strip())

for i in url_arr:
	r = requests.get(i)
	if r.status_code != 200:
		url_valid.append(i)

print(url_valid)
