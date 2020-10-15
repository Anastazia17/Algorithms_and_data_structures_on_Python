"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
print(func_1())

def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'
print(func_2())

# Делаем профилировку каждого алгоритма через timeit:

print(timeit("""
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
"""))
# Время выполнения функции: 0.0548288 мс

print(timeit("""
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'
"""))
# Время выполнения функции: 0.05943910000000001 мс
# Вывод: быстрее оказанся первый вариант (func_1).

# Пишем свой вариант:

def func_3():
    n = 0
    num = []
    max_frq = 1
    for i in range(n - 1):
        frq = 1
        for k in range(i + 1, n):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]
    if max_frq > 1:
        print(max_frq, 'раз(а) встречается число', num)
    else:
        print('Все элементы уникальны')
print(func_3())

# Делаем профилировку алгоритма через timeit:

print(timeit("""
def func_3():
    n = 0
    num = []
    max_frq = 1
    for i in range(n - 1):
        frq = 1
        for k in range(i + 1, n):
            if arr[i] == arr[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]
    if max_frq > 1:
        print(max_frq, 'раз(а) встречается число', num)
    else:
        print('Все элементы уникальны')
"""))
# Время выполнения функции: 0.059002200000000005 мс
# Данный вариант оказался дольше по времени выполнения, чем варианты выше.
# Он нам не подходит.

# Пробуем другой вариант:

def func_4(a_list: list) -> tuple:
    max_tuple = (0, a_list[0])  # Кортеж (сколько раз встречается, какое число)
    for element in a_list:
        count = a_list.count(element)
        if count > max_tuple[0]:
            max_tuple = (count, element)
    return max_tuple
a_l = [1, 2]
counts = func_4(a_l)
print(f'Чаще всех повторяется {counts}, число повторяется {counts} раз')

# Делаем профилировку алгоритма через timeit:

print(timeit("""
def func_4(a_list: list) -> tuple:
    max_tuple = (0, a_list[0])  # Кортеж (сколько раз встречается, какое число)
    for element in a_list:
        count = a_list.count(element)
        if count > max_tuple[0]:
            max_tuple = (count, element)
    return max_tuple
"""))
# Время выполнения функции: 0.1844356 мс
# Данный вариант оказался самым долгим по времени выполнения. Он нам не подходит совсем.

# Пробовала сделать через меморизацию функцию func_1, но не смогла это реализовать.

# Вывод: самый локаничный и быстрый вариант на данный момент моего решения
# так и остался первый вариант (func_1).