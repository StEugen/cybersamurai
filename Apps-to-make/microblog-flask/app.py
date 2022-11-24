from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='./template')
app.secret_key='change'
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('POSTGRESQL_DB')
db = SQLAlchemy()
db.init_app(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.Text)



@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.id.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/post', methods=["POST", "GET"])
def post():
    if request.method == "POST":
        print("Hell ya")
        article_name = request.form.get('article-name')
        print(article_name)
        text = request.form.get('article-text')
        print(text)
        return render_template('index.html', article_name=article_name,
        text=text)

    return render_template('posts.html')





if __name__ == '__main__':
    app.run()
