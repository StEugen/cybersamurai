from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todos(db.Model):
    """ Todos model """

    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(255), nullable=False)