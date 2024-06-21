"""
Разбираюсь мо сравнением времени, так как не взлетело сразу.
Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
Вынес отдельно, так как  нужно было отдебвжить

Returns:
    Приветствие, в зависимости от времени  суток
"""

import datetime


def str_to_time_conv(now_time : str):
    """
    Преобразовывает время из строки в формат datetime для корретного сравнения 

    Args:
        now_time (str):  Строка в формате 23:00:00 для преобразоывания

    Returns:
        datetime : Формат датавремени для корректного сравнения
    """
    return datetime.datetime.strptime(now_time, "%H:%M:%S").time()


print(type(datetime.datetime.now().hour))


def greeting():
    """Выводит приветствие на экран в зависимости от времени суток:
    С 6:00 до 12:00 – «Доброе утро»; С 12:00 до 18:00 – «Добрый день»
    С 18:00 до 24:00 – «Добрый вечер»; С 00:00 до 6:00 – «Доброй ночи»
    """
    # time = datetime.datetime.strptime((datetime.datetime.now().strftime("%H:%M:%S")), "%H:%M:%S").time()
    # # time = time1.strftime()
    # if (str_to_time_conv("06:00:00") <= time < str_to_time_conv("12:00:00")): return "Доброе утро"
    # if (str_to_time_conv("12:00:00") <= time < str_to_time_conv("18:00:00")): return "Добрый день"
    # if (str_to_time_conv("18:00:00") <= time < str_to_time_conv("23:59:59")): return "Добрый вечер"
    # if (str_to_time_conv("00:00:00") <= time < str_to_time_conv("06:00:00")): return "Доброй ночи"
    # else: return str(str_to_time_conv("00:06:00")) #"Фигня какая-то"
    # # return str(str_to_time_conv("06:00:00"))
    
    time = datetime.datetime.now().hour
    # time = time1.strftime()
    if 6 <= time < 12: times_greeting = "Доброе утро"
    elif 12 <= time < 18: times_greeting = "Добрый день"
    elif 18 <= time < 23: times_greeting = "Добрый вечер"
    elif 23 <= time < 6: times_greeting = "Доброй ночи"
    else: times_greeting = "Фигня какая-то "
    return times_greeting
    
if __name__=="__main__":
    print(greeting())
    
    
    
    """_summary_
    Все оказалось проще:
    
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 12:
        greeting = 'Доброе утро'
    elif now.hour >= 12 and now.hour < 18:
        greeting = 'Добрый день'
    elif now.hour >= 18 and now.hour < 24:
        greeting = 'Добрый вечер'
    else:
        greeting = 'Доброй ночи'
    
    
    Так как hour возврящает просто int... :^(
        
    """
    