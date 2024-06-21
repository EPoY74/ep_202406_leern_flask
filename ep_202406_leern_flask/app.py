"""
Автор: Евгений Петров
p174@mail.ru
Дата: 06 июня 2024  года
Цель: изучение фреймворка  Flask
Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
дополнительная информация: https://habr.com/ru/articles/193260/
"""
import datetime

from flask import Flask, request, render_template

from models import Artist, Album, Song, db


def str_to_time_conv(now_time : str):
    """
    Преобразовывает время из строки в формат datetime для корретного сравнения 

    Args:
        now_time (str):  Строка в формате 23:00:00 для преобразоывания

    Returns:
        datetime : Формат датавремени для корректного сравнения
    """
    return datetime.datetime.strptime(now_time, "%H:%M:%S").time()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:зфыыцщкв@127.0.0.1:5432/music'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Связываем приложение и экземпляр SQLAlchemy
db.init_app(app)
    
@app.route('/')  # Устанавливаем маршрут
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


@app.route("/songs")
def Songs():
    """
    Выводит список песен из БД
    """
    song_list = Song.query.all() # Делаю запрос в БД, вывести список песен
    return render_template('songs.html', songs = song_list)

@app.route("/greeting")
def greeting():
    """Выводит приветствие на экран в зависимости от времени суток:
    С 6:00 до 12:00 – «Доброе утро»; С 12:00 до 18:00 – «Добрый день»
    С 18:00 до 24:00 – «Добрый вечер»; С 00:00 до 6:00 – «Доброй ночи»
    """
    time = datetime.datetime.now().hour
    # time = time1.strftime()
    if 6 <= time < 12: times_greeting = "Доброе утро"
    elif 12 <= time < 18: times_greeting = "Добрый день"
    elif 18 <= time < 23: times_greeting = "Добрый вечер"
    elif 23 <= time < 6: times_greeting = "Доброй ночи"
    else: times_greeting = "Фигня какая-то "
    return render_template("greeting.html", text_of_greeting = times_greeting) # times_greeting
    

if __name__ == '__main__': # Проверяем, модуль или самостотельная программа
    app.run(debug=True)    # Запускаю программу
