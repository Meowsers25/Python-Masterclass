import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.buttonwoodsbrewery.com/'
driver = webdriver.Firefox()
driver.get(url)