import os.path

from flask import Flask,render_template
from flask import send_from_directory

app = Flask(__name__)

#HOMEPAGE ROUTE
@app.route('/')
def home():
    return render_template('index.html')

#HOMEPAGE ROUTE
@app.route('/about')
def about():
    return render_template('about.html')

#HOMEPAGE ROUTE
@app.route('/events')
def events():
    return render_template('events.html')

# contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
