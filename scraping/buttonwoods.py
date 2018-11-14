import requests
import bs4
import lxml
import html5lib

page = requests.get('https://www.buttonwoodsbrewery.com/').text
soup = bs4.BeautifulSoup(page, 'lxml')
# print(soup.prettify())
para = soup.find_all('div', {'id':'block-5a510f550d9297f9a56f0d5a'})
for x in para:
    tester = x.select("p:nth-of-type(3)")
    for i in tester:
        print(i.text)

    
    

# print(para)
