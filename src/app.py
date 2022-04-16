from flask import Flask, render_template, request

app = Flask(__name__)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/form')
def temp():
    user = User(
        request.args.get('name'),
        request.args.get('age')
    )
    return render_template('form.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
