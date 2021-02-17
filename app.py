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
def about_us():
    return render_template('about_us.html')

@app.route('/applications')
def applications():
    return render_template('applications.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/tech_support')
def tech_support():
    return render_template('tech_support.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/products/fans_blowers')
def products_fans_blowers():
    return render_template('products_fans_blowers.html')

@app.route('/products/heatsink')
def products_heatsink():
    return render_template('products_heatsink.html')

@app.route('/products/industrial_automation')
def products_industrial_automation():
    return render_template('products_industrial_automation.html')

@app.route('/products/motor_components')
def products_motor_components():
    return render_template('products_motor_components.html')

@app.route('/products/motors')
def products_motors():
    return render_template('products_motors.html')

@app.route('/products/power_supplies')
def products_power_supplies():
    return render_template('products_power_supplies.html')

@app.route('/products/wire_harness')
def products_wire_harness():
    return render_template('products_wire_harness.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)