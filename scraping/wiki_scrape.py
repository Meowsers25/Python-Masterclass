import requests
import lxml
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Room_641A')
soup = bs4.BeautifulSoup(res.text, 'lxml')
titles = soup.select('.mw-headline')
for i in titles:
    print(i.text)
#print(titles[0].getText())