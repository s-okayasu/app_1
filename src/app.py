import string
from flask import Flask, jsonify, redirect, render_template, request, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from query import Query

app = Flask(__name__)
base_dir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
query = Query(db)

class Titles(db.Model):
    __tablename__ = 'title'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    def __init__(self, name):
        self.name = name

class Problems(db.Model):
    __tablename__ = 'problem'
    id = db.Column(db.Integer, primary_key=True)
    title_id = db.Column(db.Integer)
    name = db.Column(db.Text)
    input_data = db.Column(db.Text)
    expect_output_data = db.Column(db.Text)
    status = db.Column(db.Text)
    def __init__(self, title_id, name, input_data, expect_output_data, status):
        self.title_id = title_id
        self.name = name
        self.input_data = input_data
        self.expect_output_data = expect_output_data
        self.status = status

@app.route('/')
def index():
    # 画面表示用のデータを設定
    screen_data = []
    titles = query.select_all(Titles)
    problems = query.select_all(Problems)
    for t_data in titles:
        title = {'id': t_data.id, 'name': t_data.name, 'problems': []}
        for p_data in problems:
            if t_data.id == p_data.title_id:
                problem = {'id': p_data.id, 'name': p_data.name, 'status': p_data.status, 'input_data': p_data.input_data,
                    'expect_output_data': p_data.expect_output_data}
                title['problems'].append(problem)
        screen_data.append(title)
    return render_template('program_execution.html', screen_data=screen_data)

@app.route('/problem_register')
def move():
    return render_template('problem_register.html')

@app.route('/problem', methods=['POST'])
def regist():
    # 入力されたtitleがDBに存在するか判定
    # 存在しない場合は追加
    title_name = request.form.get('title_name')
    result = query.select_title(Titles, title_name)
    if len(result) == 0:
        query.insert(Titles(title_name))
    # problemを追加
    title_id = query.select_title(Titles, title_name)[0].id
    print(str(title_id))
    problems = Problems(
        title_id,
        request.form.get('problem_name'),
        request.form.get('input_data'),
        request.form.get('expect_output_data'),
        '0'
    )
    query.insert(problems)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
