from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import requests
import bs4
import lxml



app = Flask(__name__)

@app.route("/")
def index():
    res = requests.get('https://www.tiltedbarnbrewery.com/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    titles = soup.select('.sqs-block-content p')
    pours = titles[3].text 
    cans = titles[4].text
    return render_template(
        'barn.html', **locals()) # **locals() passes multiple variables

@app.route("/about")
def about():
    res = requests.get('https://www.proclamationaleco.com/this-week-at-proc/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    titles = soup.select('.et_pb_text_5')
    pours = titles[0].text
    return render_template('about.html', pours)
    


if __name__ == "__main__":
    app.run(debug=True)