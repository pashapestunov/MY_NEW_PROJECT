from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # отслеживаем главную страницу
@app.route('/home')  # второй декоратор для вывода такой-же инфы на стр home
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":  # мы указываем, что этот файл основной
    app.run(debug=True)     # app запускает программу. дебаг - все ошибки показываются на сайте






