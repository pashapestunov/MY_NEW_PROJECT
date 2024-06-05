from flask import Flask, render_template, url_for, redirect
from flask import request

app = Flask(__name__)

# @app.route('/submit', methods=['POST'])
# def submit():
#   name = request.form['name']
#   sex = request.form['sex']
#   return f'Hello, {name}, {sex}'
#
# @app.route('/hello/')
# @app.route('/hello/<name>')  # отслеживаем главную страницу
# def hello(name=None):
#     return (render_template("test_f1.html", name=name))
#


@app.route('/')  # отслеживаем главную страницу
def index():
    return render_template("test_f1.html")


@app.route('/test_f1_enter.html')
def test_f1_enter():
    return render_template("test_f1_enter.html")


@app.route('/test_f1.html')
def back_from_enter():
    return render_template("test_f1.html")


@app.route('/test_f1_registration.html')
def test_f1_registration():
    return render_template("test_f1_registration.html")


if __name__ == "__main__":  # мы указываем, что этот файл основной
    app.run(debug=True)     # app запускает программу. дебаг - все ошибки показываются на сайте

