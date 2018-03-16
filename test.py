import requests
from bs4 import BeautifulSoup



r = requests.get("https://www.voachinese.com/a/a-21-n2007-03-12-voa44-58899712/1101411.html")

def get_title(res):
	def extract (text):
		start_pos = text.find(">") + 1
		end_pos = text.find("</title>")
		return text[start_pos:end_pos]
	
	soup = BeautifulSoup(res.text, 'html.parser')
	title = extract(str(soup.title))
	return title

print(get_title(r))



