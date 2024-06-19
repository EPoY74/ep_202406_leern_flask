"""
Автор: Евгений Петров
p174@mail.ru
Дата: 17 июня 2024  года
Назначение файла: Сохдание базы даннных
Цель: изучение фреймворка  Flask
Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
"""
from flask import Flask
from models import Artist, Album, Song, db 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:зфыыцщкв@127.0.0.1:5432/music'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # print("Создание таблиц завершено")