"""
Автор: Евгений Петров
p174@mail.ru
Дата: 06 июня 2024  года
Цель: изучение фреймворка  Flask
Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')  #Устанавливаем маршрут
def home():  # Это будет отображаться
    """
    это стартовая страница
    """
    return 'Это галвная страница'


@app.route ('/about')
def about():
    """
    Об авторе блок
    """
    return 'Здесь будет информация об авторе сайта'   


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
    

if __name__ == '__main__': # Проверяем, модуль или самостотельная программа
    app.run()  # Запускаю программу

