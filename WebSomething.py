import requests as rq
from bs4 import BeautifulSoup as soup

URL = "https://en.wikipedia.org/wiki/Chocolate"
text = rq.get(URL).text

data = soup(text, "html5lib")
element = data.find(id="mv-content-text")

for i in range(1, len(element.ul.contents), 2):
    print(element.ul.contents[i].text)