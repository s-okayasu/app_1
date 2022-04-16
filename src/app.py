from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/temp/<name>')
def temp(name):
    user = {
        'name': name
    }
    return render_template('temp.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
