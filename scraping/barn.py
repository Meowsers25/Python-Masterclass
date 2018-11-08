import requests
import bs4
import lxml

res = requests.get('https://www.tiltedbarnbrewery.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
titles = soup.select('.sqs-block-content p')
print(titles[3].text)
print(titles[4].text)
