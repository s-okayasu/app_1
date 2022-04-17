from flask import Flask, redirect, render_template, request, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from crud import Crud

app = Flask(__name__)
base_dir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
crud = Crud(db)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/')
def index():
    users = crud.read(User)
    is_recode = db.session.query(func.count(User.id)).first()[0] > 0
    print(db.session.query(func.count(User.id)).first()[0])
    print(is_recode)
    return render_template('list.html', users=users, is_recode=is_recode)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/create')
def temp():
    user = User(
        request.args.get('name'),
        request.args.get('age')
    )
    crud.create(user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
