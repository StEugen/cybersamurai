from flask import Flask, request, render_template, redirect, url_for

from model import db, Todos


app = Flask(__name__, template_folder='./template')
app.secret_key = 'change'
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db.init_app(app)

@app.route('/')
def index():
    todos = db.session.query(Todos).order_by(Todos.id.desc()).all()
    return render_template('index.html', todos=todos)

@app.route('/addtask', methods=["POST"])
def addtask():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        
        todo = Todos(title=title, content=content)
        
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = Todos.query.filter_by(id=id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todos.query.filter_by(id=id).first()
    if request.method == "POST":
        todo.title = request.form['title']
        todo.content = request.form['content']
        
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('edit.html', todo=todo)

if __name__ == '__main__':
    app.run()
