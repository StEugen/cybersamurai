from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='./template')
app.secret_key='change'
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('POSTGRESQL_DB')
db = SQLAlchemy(app)
db.init_app(app)


class blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.Text)



@app.route('/')
def index():
    posts = blogpost.query.order_by(blogpost.id.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/add')
def add():
    return render_template('addpost.html')

@app.route('/addpost', methods=["POST", "GET"])
def addpost():
    title = request.form['title']
    content = request.form['content']
    post = blogpost(title=title, content=content)
    
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run()
