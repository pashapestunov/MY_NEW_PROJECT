from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # отслеживаем главную страницу
def index():
    return render_template("test_f1.html")


if __name__ == "__main__":  # мы указываем, что этот файл основной
    app.run(debug=True)     # app запускает программу. дебаг - все ошибки показываются на сайте

