from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/lobby')
def lobby():
    data = {'title', 'Hello'}
    return render_template('lobby.html', context=data)
