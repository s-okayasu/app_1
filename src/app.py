from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import shutil
from query import Query
from execute_program import execute

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
    try:
        # 画面表示用のデータを設定
        screen_data = []
        titles = query.select_all(Titles)
        problems = query.select_all(Problems)
        for t_data in titles:
            title = {'id': t_data.id, 'name': t_data.name, 'problems': []}
            for p_data in problems:
                status = ''
                if p_data.status == '1':
                    status = 'CLEAR'
                if t_data.id == p_data.title_id:
                    problem = {'id': p_data.id, 'name': p_data.name, 'status': status, 
                    'input_data': p_data.input_data, 'expect_output_data': p_data.expect_output_data}
                    title['problems'].append(problem)
            screen_data.append(title)
    except Exception as ex:
        print(ex)
    return render_template('program_execution.html', screen_data=screen_data)

@app.route('/problem_register')
def move():
    return render_template('problem_register.html')

@app.route('/result')
def get():
    try:
        id = request.args.get('id', '', type=int)
        expect_output = request.args.get('output', '', type=str)
        input_str = request.args.get('input', '', type=str)
        print('info log : id=' + str(id))
        print('info log : input=' + input_str)
        print('info log : expect_output=' + expect_output)
        # プログラム実行
        input_list = input_str.split(' ')
        output = execute.exec(input_list)
        result = 'False'
        if output == expect_output:
            result = 'True'
            # statusを更新
            query.update_status(Problems, id)
            # ファイル移動
            shutil.move('./execute_program/execute.py', './clear_problems/')
            os.rename('./clear_problems/execute.py', './clear_problems/problemId_' + str(id) + '.py')
            shutil.copy('./execute_program/template_file/template.py', './execute_program/')
            os.rename('./execute_program/template.py', './execute_program/execute.py')
    except Exception as ex:
        print(ex)
    return jsonify({'result': result, 'code_output': output})

@app.route('/problem', methods=['POST'])
def regist():
    try:
        title_name = request.form.get('title_name')
        problem_name = request.form.get('problem_name')
        input_data = request.form.get('input_data')
        expect_output_data = request.form.get('expect_output_data')
        print('info log : problem_name=' + title_name)
        print('info log : problem_name=' + problem_name)
        print('info log : input_data=' + input_data)
        print('info log : expect_output_data=' + expect_output_data)
        # 入力されたtitleとproblemがDBに存在するか判定
        # 両方が同時に存在する場合は追加しない
        title = query.select_title(Titles, 'name', title_name)
        problem = query.select_title(Titles, 'name', problem_name)
        if len(title) > 0 and len(problem) > 0:
            return render_template('problem_register.html', is_regist=True, message='既に登録済みです。')
        if len(title) == 0:
            # titleを追加
            query.insert_recode(Titles(title_name))
        if len(problem) == 0:
            print('problem')
            # problemを追加
            title_id = query.select_title(Titles, 'name', title_name)[0].id
            problems = Problems(
                title_id,
                request.form.get('problem_name'),
                request.form.get('input_data'),
                request.form.get('expect_output_data'),
                '0'
            )
            query.insert_recode(problems)
    except Exception as ex:
        print(ex)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
