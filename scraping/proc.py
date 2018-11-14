import requests
import bs4
import lxml
# from bs4 import BeautifulSoup

res = requests.get("https://www.proclamationaleco.com/this-week-at-proc/")
soup = bs4.BeautifulSoup(res.content, 'html.parser')
print(soup)

    