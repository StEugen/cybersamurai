from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='./template')



@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)