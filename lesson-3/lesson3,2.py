"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def my_func(name, surname, year, city, email, number):
    print(name, surname, year, city, email, number)


my_func(name='Иван ', surname='Иванов ', year='2000 ',
        city='Москва ', email='NN@mail.ru ', number='911 ')