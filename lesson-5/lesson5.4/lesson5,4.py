"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open("lesson-5/lesson5.4/lesson5,4.txt", "r+") as f1:
    a = list()
    for k in f1.readlines():
        a.extend(k.rstrip().split(" "))

print("Менее 20 000р у: ")
summ = 0
for i in range(1, len(a), 2):
    por = float(a[i])
    summ += por
    ca = len(a) / 2
    if por < 20000:
        print(a[i - 1])
av = summ / ca
print(f"\nСредняя величина дохода сотрудников: {av}")