"""
Автор: Евгений Петров
p174@mail.ru
Дата: 17 июня 2024  года
Цель: изучение фреймворка  Flask
Назначение файла: Создаем модели для БД
Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
"""


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Artist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
     
        
class Album(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    year = db.Column(db.String(4), nullable = False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable = False)
    artist =  db.relationship('Artist', backref = db.backref('albums', lazy = True))
    

class Song(db.Model):
    # TODO КМК артиста надо добавить, иначе, чтобв посмотреть кто поет  - понадобиться каждый раз скакать по таблицам
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    lenght = db.Column(db.String(4), nullable = False)
    track_number = db.Column(db.String(4), nullable = False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable = False)
    album = db.relationship('Album', backref = db.backref('songs' , lazy = True))
    
    
