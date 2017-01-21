from bs4 import BeautifulSoup as soup
import requests as rq

html = rq.get("https://en.wikipedia.org/wiki/Ancient_Egypt")
data = soup(html.text, "html5lib")
toc = data.find(id="toc")
toc = toc.text
print(toc)