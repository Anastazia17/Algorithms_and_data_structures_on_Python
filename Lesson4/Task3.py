"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
from timeit import timeit

# Делаем профилировку каждого алгоритма через cProfile:

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def main():
    revers(5)
    revers_2(5)
    revers_3(5)

cProfile.run('main()')

"""
Результат:

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      2/1    0.000    0.000    0.000    0.000 Task3.py:16(revers)
        1    0.000    0.000    0.000    0.000 Task3.py:25(revers_2)
        1    0.000    0.000    0.000    0.000 Task3.py:32(revers_3)
        1    0.000    0.000    0.000    0.000 Task3.py:37(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Функции очень быстро выполнились, поэтому время выполнения везде равно нулю.
# Единственный вывод можно сделать по функции revers, что у нее было 2 вызова,
# вместо одного, как у остальных функций.


# Делаем профилировку каждого алгоритма через через timeit:

print(timeit("""def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
"""))
# Время выполнения функции: 0.07643130000000001

print(timeit("""def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
"""))
# Время выполнения функции: 0.04995099999999998

print(timeit("""def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
"""))
# Время выполнения функции: 0.0544336

# Здесь уже более явная картина.
# Первая функция (revers) самая медленная,
# вторая функция (revers_2) средняя по времени выполнения,
# соответственно, третья функция (revers_3) самая быстрая в выполнении.