import requests
import sys
from bs4 import BeautifulSoup
from openpyxl import Workbook 
import re

script, url_filename = sys.argv
# get the url list from the file given by user after the script name.
Subdomain_list = []
# subdomain_dic will be like "{' chao': ['http://www.baidu.com', 'http://sina.cn', 'http://qq.com', 'http://jd.com'], ' hello': ['http://www.taobao.com']}"
subdomain_dic = {}
def get_url_list (url_file):
	with open(url_file, "r", encoding = "utf-8") as f:
		line_list = list(f)
		if line_list[0].find("Subdomain") == -1:
			print("there's no subdomain")
			subdomain_dic[url_file] = []
			for i in line_list:
				subdomain_dic[url_file].append(i.strip())
		else:
			for i in line_list:
				if i.find("Subdomain") != -1:
					Subdomain_list.append(i[12:].strip())
					subdomain_dic[Subdomain_list[len(Subdomain_list)-1]] = []
				else: 
					subdomain_dic[Subdomain_list[len(Subdomain_list)-1]].append(i.strip())			
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


a = get_url_list(url_filename)
print(a)
for i,j in a.items():
	a[i] = url_test(j)
	print(a[i])


wb = Workbook()
for i,j in a.items():
	if i.find("/") != -1:
		i = "root"
	ws = wb.create_sheet(i)
	for m,n in j.items():
		ws.append([m,n])

wb.save(url_filename+'.xlsx')
