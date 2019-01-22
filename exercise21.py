import requests
from bs4 import BeautifulSoup

def make_txt_from_url(url_source):
	r = requests.get(url_source)
	r_html = r.text
	name_of_file = input("Please give your new text file a name >> ")

	soup = BeautifulSoup(r_html, "html.parser")
	f = open(f"{name_of_file}.txt", "w+", encoding="utf-8")

	for content in soup.find_all("p"):
		f.write(str(content.text))

if __name__ == "__main__":
	url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
	make_txt_from_url(url)	