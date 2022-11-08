from crypt import methods
from flask import redirect
from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__, template_folder='./template')

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        print(request.form.getlist('check'))
        return 'Done'
    return render_template('index.html')


