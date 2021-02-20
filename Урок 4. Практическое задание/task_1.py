"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


num_list = [el + 10 for el in range(1, 10000)]

# Проведем замеры времени:
print(timeit('func_1(num_list)', globals=globals(), number=1000))


# А теперь оптимизируем функцию:
def func_2(nums):
    return [el for el in nums if el % 2 == 0]


# Проведем замеры времени:
print(timeit('func_2(num_list)', globals=globals(), number=1000))

'''
По итогу, оптимизировал функцию, выполнив ее через списковое включение, так как этот вариант
является более ускоренной и компактной возможностью создания списка в Python.
'''
