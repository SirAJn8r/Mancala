import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as soup
import requests as rq
from collections import Counter
html = rq.get("http://terraria.gamepedia.com/Bat_Scepter")
data = soup(html.text, "html5lib")
table = data.find(class_='infobox')
tbody = table.find('tbody')
tr = tbody.findAll('tr')

td = []
start = 0
while(start < len(tr)):
    print(soup.text(tr[start].findAll('th')))
    start += 1

print(td)