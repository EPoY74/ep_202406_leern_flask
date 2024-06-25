"""
Разбираюсь мо сравнением времени, так как не взлетело сразу.
Тестовй файл, буду в нем ковырять и тыкать палкой

Сайт урока: https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-23-osnovy-veb-razrabotki-na-flask-2023-06-27
Вынес отдельно, так как  нужно было отдебвжить

Returns:
    Приветствие, в зависимости от времени  суток и не только
    
    
"""

import datetime


import requests as reqs


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
    

def my_api_request():

    """Работаю и изучаю реквесты.
       Сайт урока: https://proglib.io/p/python-i-api-prevoshodnoe-kombo-dlya-avtomatizacii-raboty-s-publichnymi-dannymi-2021-02-26
    """
    responce_request = reqs.get("https://randomuser.me/api/")
    # responce_request = reqs.get("")
    return  responce_request
    
if __name__=="__main__":
       # print(greeting())
    print(my_api_request().text)
    print(my_api_request().request.url)
    

    all_attributes = dir(my_api_request().request)
    
    print(type(all_attributes))
    
    for index_of_attribute, attribute in enumerate(all_attributes, start = 1):
        print(f"{index_of_attribute}: {attribute}")
    
    for index, attribute in enumerate (all_attributes):
        if attribute.find("_") == 0:
            all_attributes[index] = " "
    
    for index_of_attribute, attribute in enumerate(all_attributes, start = 1):
        print(f"{index_of_attribute}: {attribute}")
    
    print(20*"_")   
    
    clear_list = [attribute for attribute in all_attributes if len(attribute) != 1 and attribute != " "]
        
    print(20*"_")
    
    for index_of_attribute, attribute in enumerate(clear_list, start = 1):
        print(f"{index_of_attribute}: {attribute}")
        
    print(20*"_")

    # #Выведите их на экран
    # for index_of_atribute, attribute in enumerate(all_attributes, statr = 1):
    #     # print(attribute + " "+ my_api_request().str(attribute))
    #     if attribute.index("_"):
    #         continue
        
    #     value = str(getattr(my_api_request, attribute))
    #     print(f"{index_of_atribute}: my_api_request().{attribute}: {value}")
        
