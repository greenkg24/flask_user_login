from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

import sqlite3

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)