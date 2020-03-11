from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('/about/about.jinja', title="About")

@app.route('/portfolio')
def portfolio():
    return render_template('/portfolio/portfolio.jinja', title="Portfolio")

@app.route('/blog')
def blog():
    return render_template('/blog/blog.jinja', title="Blog")

@app.route('/contact')
def contact():
    return render_template('/contact/contact.jinja', title="Contact")