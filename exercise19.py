import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")


for content in soup.find_all("p"):
	print(content.text)

