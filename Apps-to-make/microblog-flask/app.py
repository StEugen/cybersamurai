from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__, template_folder='./template')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=["POST", "GET"])
def post():
    if request.method == "POST":
        print("Hell ya")
        article_name = request.form.get('article-name')
        print(article_name)
        text = request.form.get('article-text')
        print(text)
        res = render_template(
            'page.html', title=article_name,
            article=text
        )
        return res

    return render_template('posts.html')





if __name__ == '__main__':
    app.run()
