"""
Разбираюсь мо сравнением времени, так как не взлетело сразу.
Тестовй файл, буду в нем ковырять и тыкать палкой

Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
Вынес отдельно, так как  нужно было отдебвжить

Returns:
    Приветствие, в зависимости от времени  суток и не только
    
    
"""

import datetime
import os
import sys


import requests as reqs


def cls():
    """Отчищает экран
    """
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        print("Не могу определить операционную системя для корректной очистки экрана")
        

def str_to_time_conv(now_time : str):
    """
    Преобразовывает время из строки в формат datetime для корретного сравнения 
    Args:
        now_time (str):  Строка в формате 23:00:00 для преобразоывания
    Returns:
        datetime : Формат датавремени для корректного сравнения
    """
    return datetime.datetime.strptime(now_time, "%H:%M:%S").time()


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
    # Добавил дополнительное  значение на всякий случай
    else: times_greeting = "Фигня какая-то "
    
    return times_greeting
    

def my_api_request(my_api_sitename : str):

    """Работаю и изучаю реквесты.
    Функция  возвращает объект типа request, полученные от сайта 
       Сайт урока: https://proglib.io/p/python-i-api-prevoshodnoe-kombo-dlya-avtomatizacii-raboty-s-publichnymi-dannymi-2021-02-26
    """
    responce_request = reqs.get(my_api_sitename)
    # responce_request = reqs.get("")
    return  responce_request


def dividing_line_20():
    """Выводит разделительную линию из 20 символов "-"
    """
    print(20*"-")  
 
    
def print_responce_attributs(site_responce):
    """Выводит на экран пронумерованый список  не приматных атрибутов у возвращенного запроса

    Args:
        site_responce (_type_):  Ответ сайта
    """
    for index_of_attribute, attribute in enumerate(site_responce, start = 1):
        print(f"{index_of_attribute}: {attribute}")
    


def clear_func_args(site_responce):
    """Подготавлию данные для вывода только официально доступных полей
       и вывожу их в консоль, а может и буду позже просто возвращать

    Args:
        responce (_type_): Ответ (часть, которая responce) сайта
    """
    print_responce_attributs(site_responce)
    
    for index, attribute in enumerate (site_responce):
        if attribute.find("_") == 0:
            site_responce[index] = " "
    
    print_responce_attributs(site_responce)
    dividing_line_20() 

    #Используя list comprehension убираем заранее попеняные позиции (меняли ранее на пробелы)
    clear_list = [attribute for attribute in all_attributes if len(attribute) != 1 and attribute != " "]
        
    dividing_line_20()
    
    print_responce_attributs(clear_list)  
    dividing_line_20()

    
def clear_private_arguments(site_responce):
    """Убирает приватные аргументы у возврещенного ответа с помощью list comprehension

    Args:
        site_responce (_type_): Ответ сайта , где необходимо вывести аргументы
    """
    
    clear_list = [attribute for attribute in site_responce if attribute[0] != "_"]

    return clear_list
    
        
if __name__=="__main__":
    
    is_cls = input("Очистить экран? (y/n): ")
    if is_cls.upper() == "Y":
        cls()

    APISITENAME : str= "https://randomuser.me/api/"
y
    # Получаю отает от сайта
    site_responce = my_api_request(APISITENAME)
    
    # Вывожу на экран, то что получил от сайта
    print(site_responce.text)
    
    # Вывожу на экран служебную инормацию запроса, т.е. URL сайта
    print(site_responce.request.url)
    
    # Получаю список всех атрибутов полученного запроса
    all_attributes = dir(site_responce.request)
    
    print(type(all_attributes))

    dividing_line_20()
    
    all_clear_attributes = clear_private_arguments(all_attributes)
    print_responce_attributs(all_clear_attributes)
    # clear_func_args(all_attributes)
    
    dividing_line_20()

    # Вывожу пронумерованый  список не приватных аргументов
    for index, attribute in enumerate(all_clear_attributes, start=1):
        # получаем значение атрибута по его имени
        value = getattr(site_responce.request, attribute)
        print(f"{index}. {attribute}: {value}")
    
            
