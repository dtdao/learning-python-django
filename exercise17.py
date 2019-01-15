import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
for article in soup.find_all("h2", class_="esl82me2"):
	print(article.text)

# for title in soup.find_all("h2"):
# 	print(title.text)