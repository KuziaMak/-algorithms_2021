"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
comp = [["Evil componi", 12231], ["Good componi", 12566471], ["Normal componi", 446231], ["Bad componi", 2281],
        ["min componi", 1264]]


def zad1(com):  # T(N^2+16N+6) O(N^2)
    number = [x[1] for x in com]  # 1 + N
    comp, fin = [], []  # 2
    for i in range(3):  # 3(
        comp.append(max(number))  # 1 + N
        del number[number.index(max(number))]  # N + N + N)
    for j in com:  # N(
        if j[1] in comp:  # 1+N+1
            fin.append(j)  # 1)
    return fin  # 1


print(zad1(comp))


def zad2(com):  # T(NLogN +6N + 1) O(NlogN)
    comp = {}  # 1
    for i in com:  # N(
        comp[i[0]] = i[1]  # 1+1+1 )
    return sorted(comp.items(), key=lambda x: x[1], reverse=True)[:3]  # NlogN +N+N+N


print(zad2(comp))

"""Вывод: Второй лудшее чем первый. Так как в первом слишком много действий связоное с циклами и поиском, 
а во втором даже меньше код по длинне и меньше действий. Но все же они оба плохи не знаю о чем думал когда их делал
 но сейчас смерился с их существованием"""
