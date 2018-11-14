from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

import requests
import bs4
import lxml

app = Flask(__name__)

@app.route('/')
def index():
    res = requests.get('https://www.proclamationaleco.com/this-week-at-proc/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # return "Hello World"
    titles = soup.select('.et_pub_text_inner')
    test = titles[0].text
    return test
    

if __name__ == "__main__":
    app.run(debug=True)