"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import timeit
from random import randint
from statistics import median


def no_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


def gnome_sort(sort_list):
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list

def gnome_median(sort_list):
    return gnome_sort(sort_list)[len(sort_list) // 2]


m = int(input('Введите m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{orig_list}\n')


# Находим медиану через встроенную функцию:
print(f'Медиана (встроенная функция): {median(orig_list)}')

# Находим медиану без сортировки исходного массива:
print(f'Медиана (без сортировки): {no_sort(orig_list)}')

# Находим медиану с сортировкой исходного массива:
print(f'Медиана (с сортировкой): {gnome_sort(orig_list)[m]}')


# Делаем замеры:
print(timeit.timeit("median(orig_list[:])", setup="from __main__ import orig_list, median", number=10000))
print(timeit.timeit("no_sort(orig_list[:])", setup="from __main__ import orig_list, no_sort", number=10000))
print(timeit.timeit("gnome_sort(orig_list[:])", setup="from __main__ import orig_list, gnome_sort", number=10000))


# Результат:
# Введите m: 10
# Исходный массив:
# [91, 65, 71, 82, 96, 45, 87, 17, 98, 20, 8, 14, 57, 63, 61, 83, 66, 62, 100, 56, 74]
#
# Медиана (встроенная функция): 65
# Медиана (без сортировки): 65
# Медиана (с сортировкой): 65
# 0.0063230000000000786
# 0.7578280999999998
# 0.022950600000000154


# Вывод: быстрее всего оказалась встроенная функция, как и ожидалось.
# Самая медленная, конечно же, стала функция поиска медианы без сортировки,
# так как получается слишком много повторных проходов в ходе выполнения кода.
# Про функцию поиска медианы с помощью Gnome можно сказать, что было очевидно,
# что встроенные функции практически во всех случаях работают быстрее.