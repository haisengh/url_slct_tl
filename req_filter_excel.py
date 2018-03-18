import requests
import sys
from bs4 import BeautifulSoup
from openpyxl import Workbook 

# script, url_filename = sys.argv
# get the url list from the file given by user after the script name.
subdomain_list = []
# subdomain_dic will be like "{' chao': ['http://www.baidu.com', 'http://sina.cn', 'http://qq.com', 'http://jd.com'], ' hello': ['http://www.taobao.com']}"
subdomain_dic = {}
def get_url_list (url_file):
	index = -1
	with open(url_file, "r", encoding = "utf-8") as f:
		for i in f:
			url = i.strip()
			if url[0:9] == "Subdomain":
				index = index + 1
				subdomain_list.append(url[11:])
				subdomain_dic[subdomain_list[index]] = []
			else:
				subdomain_dic[subdomain_list[index]].append(url)
				
	return subdomain_dic

# test the availability of each url in the url_list.
def url_test (url_list):
	# code_dic is the dic describing the status code of each url.
	title_dic = {}
	code_dic = {}
	err_list = []
	for i in url_list:
		try:
			r = requests.get(i)
			code_dic[i] = r.status_code
			if code_dic[i] == 200: 
				title_dic[i] = BeautifulSoup(r.text, 'html.parser').title.string

		except:
			err_list.append(i)
	return title_dic


a = get_url_list("txt/sample_url.txt")
print(a)
for i,j in a.items():
	a[i] = url_test(j)
	print(a[i])


wb = Workbook()
for i,j in a.items():
	ws = wb.create_sheet(i)
	for m,n in j.items():
		ws.append([m,n])

wb.save('sample.xlsx')
