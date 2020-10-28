"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit


# Стандартный подход:
def bubble_sort(new_list):
    n = 1
    while n < len(new_list):
        for i in range(len(new_list)-n):
            if new_list[i] < new_list[i+1]:
                new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
        n += 1
    return new_list


# Подход с доработкой:
def bubble_sort_upd(new_list):
    n = 1
    k = 0
    while n < len(new_list):
        for i in range(len(new_list)-n):
            if new_list[i] < new_list[i+1]:
                new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
                k = 1
        if k == 0:
            break
        n += 1
    return new_list


new_list = [random.randint(-100, 100) for i in range(1000)]

print(timeit.timeit("bubble_sort(new_list[:])", setup="from __main__ import bubble_sort, new_list", number=100))
print(timeit.timeit("bubble_sort_upd(new_list[:])", setup="from __main__ import bubble_sort_upd, new_list", number=100))


# Результат стандартного подхода: 7.588146 мс
# Результат подхода с доработкой: 8.045193900000001 мс


# Вывод: по времени все равно выиграл стандартный подход,
# так как в нем отсутствует лишняя проверка на отсутствие сортировки.