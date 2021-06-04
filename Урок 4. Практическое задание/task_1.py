"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit

arr = [x for x in range(1000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1(arr)", globals=globals(), number=10000))


def func_2(nums): return [x for x in nums if x % 2 == 0]


"""
Я сделал генератор создающий новый список и дал ему условие, чтобы он брал четные элементы
(т.е. выдавал True при вызове x % 2 == 0) из получаймого списка.
Тем самым сделал создания списка с четными индексами чуть быстрее, чем в первом, ведь быстрее создовать список
с помощью генератора с условием, чем проверять каждый элемент по одному на четность и добавлять по одному 
в новый список.
"""

print(timeit("func_2(arr)", globals=globals(), number=10000))
print(func_1(arr))
print(func_2(arr))
