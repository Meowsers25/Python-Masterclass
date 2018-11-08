import requests
import bs4
import lxml

res = requests.get('http://www.example.com')
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml') # make a soup of the text
# print(type(soup)) 

# print(soup.select('title')) puts tags and text in a list
title_tag_list = soup.select('title')
print(title_tag_list[0].getText())