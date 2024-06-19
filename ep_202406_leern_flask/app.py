"""
Автор: Евгений Петров
p174@mail.ru
Дата: 06 июня 2024  года
Цель: изучение фреймворка  Flask
Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
дополнительная информация: https://habr.com/ru/articles/193260/
"""

from flask import Flask, request, render_template


app = Flask(__name__)
    

@app.route('/')  #Устанавливаем маршрут
def home():  # Это будет отображаться
    """
    это стартовая страница
    """
    # return 'Это галвная страница'   # А тут вывводится просто строка
    return render_template('main.html')  # Решил, что буду генерировать веб страницы, а не выводить строку в интерфейс


@app.route ('/about')
def about():
    """
    Об авторе блок
    """
    # return 'Здесь будет информация об авторе сайта'
    return render_template("about.html")


@app.route('/blog')
def blog():
    """
    Блог с иформацией о блоге
    """
    return 'Это мой блог о всяком разном'

@app.route("/user/<username>")  # Используем переменные
def  user_profile(username):
    """
    Выводит информацию о пользователе.
    Использую переменые
    """
    return f"Это профиль пользователя {username}"

@app.route("/user_id/<int:user_id>")
def user_id_profile(user_id):
    """
    Принимает значение типа int
    """
    return f"Это профиль пользователя с ID {user_id}"


@app.route("/login", methods=['GET','POST'])
def login():
    """
    Форма запроса пароля
    """
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        #Тут проверка логина и пароля
        return f"Имя пользователя: {username}, пароль: {password}"
    else:
        return render_template('login.html')

if __name__ == '__main__': # Проверяем, модуль или самостотельная программа
    app.run(debug=True)  # Запускаю программу
