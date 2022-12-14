"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def my_func():
    try:
        d = {}
        with open("lesson-5/lesson5.6/lessont5,6.txt", encoding="utf-8") as f1:
            for k in f1:
                study_items, qty = k.split(":")
                l = sum(
                    map(int, "".join([i for i in qty if i == " " or ("0" <= i <= "9")]).split()))
                d[study_items] = l
            print(f"\nСловарь: {d}")
    except FileNotFoundError:
        return print("Файл не найден(((")


my_func()
