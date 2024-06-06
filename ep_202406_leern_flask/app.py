"""
Автор: Евгений Петров
p174@mail.ru
Дата: 06 июня 2024  года
Цель: изучение фреймворка  Flask
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')  #Устанавливаем маршрут
def hello():  # Это будет отображаться
    """
    Выводит строку 'Привет Мир'
    """

    return 'Hello, world'


if __name__ == '__main__':
    app.run()
    