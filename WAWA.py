import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup as soup
import requests as rq
from collections import Counter

html = rq.get("https://www.ncdc.noaa.gov/stormevents/listevents.jsp?eventType=ALL&beginDate_mm=08&beginDate_dd=01&beginDate_yyyy=2011&endDate_mm=08&endDate_dd=31&endDate_yyyy=2016&county=KING%3A33&hailfilter=0.00&tornfilter=0&windfilter=000&sort=DT&submitbutton=Search&statefips=53%2CWASHINGTON")
data = soup(html.text, "html5lib")
table = data.find(id="results")
weather = table.findAll('td')

start = 18
occurrences = []
while(start < len(weather)-11):
    occurrences.append(weather[start].text)
    start += 12

count = Counter(occurrences)
keys = list(count.keys())
values = list(count.values())

index = np.arange(len(keys)) +0.5
fig = plt.figure(figsize=(12,9))
plt.xlabel('Number of pure unbrideled Weather')
plt.ylabel('Weather of Sorts')
plt.barh(index, values)
plt.yticks(index + 0.4, keys, size='x-small')
fig.savefig('weatherdata')