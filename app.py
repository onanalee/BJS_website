# sudo lsof -i:5000

from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.bjs

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_us')
def about():
    return render_template('about_us.html')

@app.route('/applications')
def applications():
    return render_template('applications.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/tech_support')
def timezone():
    return render_template('tech_support.html')

@app.route('/contact_us')
def exchangeRates():
    return render_template('contact_us.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)