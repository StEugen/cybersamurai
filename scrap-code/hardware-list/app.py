from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='./template')
app.secret_key = 'channge-later'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTREGSQL_DB')
db = SQLAlchemy(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)