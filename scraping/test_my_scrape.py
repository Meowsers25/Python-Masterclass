from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup = BeautifulSoup(html, "lxml")
# print(type(soup))

title = soup.title
# print(title.text)
text = soup.get_text()
# print(text)
# print(soup.find_all('a')[0])
all_links = soup.find_all('a')
for link in all_links:
    print(link.get('href'))