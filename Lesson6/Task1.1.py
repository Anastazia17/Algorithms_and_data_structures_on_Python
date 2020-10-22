from memory_profiler import profile
from functools import reduce

# 6 вариантов функции,
# которая преобразует список целых чисел в строку,
# предполагая, что эти целые числа представлены в формате ASCII.
# Например, список [97, 98, 99] должен быть преобразован в строку 'abc'.

# Вариант 1:
def func1(list):
    string = ""
    for item in list:
        string = string + chr(item)
    return string

# Вариант 2:
def func2(list):
    return reduce(lambda string, item: string + chr(item), list, "")

# Вариант 3:
def func3(list):
    string = ""
    for character in map(chr, list):
        string = string + character
    return string

# Вариант 4:
def func4(list):
    string = ""
    lchr = chr
    for item in list:
        string = string + lchr(item)
    return string

# Вариант 5:
def func5(list):
    string = ""
    for i in range(0, 256, 16):
        s = ""
        for character in map(chr, list[i:i+16]):
            s = s + character
        string = string + s
    return string

# Вариант 6:
def func6(list):
    import array
    return array.array('b', list).tostring()


# Делаем замеры:

# Вариант 1:
@profile
def func1(list):
    string = ""
    for item in list:
        string = string + chr(item)
    return string
func1([97, 98, 99])
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     18.1 MiB     18.1 MiB           1   @profile
    55                                         def func1(list):
    56     18.1 MiB      0.0 MiB           1       string = ""
    57     18.1 MiB      0.0 MiB           4       for item in list:
    58     18.1 MiB      0.0 MiB           3           string = string + chr(item)
    59     18.1 MiB      0.0 MiB           1       return string
"""

# Вариант 2:
@profile
def func2(list):
    return reduce(lambda string, item: string + chr(item), list, "")
func2([97, 98, 99])
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     18.1 MiB     18.1 MiB           1   @profile
    65                                         def func2(list):
    66     18.1 MiB      0.0 MiB           7       return reduce(lambda string, item: string + chr(item), list, "")
"""

# Вариант 3:
@profile
def func3(list):
    string = ""
    for character in map(chr, list):
        string = string + character
    return string
func3([97, 98, 99])
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    71     18.1 MiB     18.1 MiB           1   @profile
    72                                         def func3(list):
    73     18.1 MiB      0.0 MiB           1       string = ""
    74     18.1 MiB      0.0 MiB           4       for character in map(chr, list):
    75     18.1 MiB      0.0 MiB           3           string = string + character
    76     18.1 MiB      0.0 MiB           1       return string
"""

# Вариант 4:
@profile
def func4(list):
    string = ""
    lchr = chr
    for item in list:
        string = string + lchr(item)
    return string
func4([97, 98, 99])
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    81     18.1 MiB     18.1 MiB           1   @profile
    82                                         def func4(list):
    83     18.1 MiB      0.0 MiB           1       string = ""
    84     18.1 MiB      0.0 MiB           1       lchr = chr
    85     18.1 MiB      0.0 MiB           4       for item in list:
    86     18.1 MiB      0.0 MiB           3           string = string + lchr(item)
    87     18.1 MiB      0.0 MiB           1       return string
"""

# Вариант 5:
@profile
def func5(list):
    string = ""
    for i in range(0, 256, 16):
        s = ""
        for character in map(chr, list[i:i+16]):
            s = s + character
        string = string + s
    return string
func5([97, 98, 99])
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    92     18.1 MiB     18.1 MiB           1   @profile
    93                                         def func5(list):
    94     18.1 MiB      0.0 MiB           1       string = ""
    95     18.1 MiB      0.0 MiB          17       for i in range(0, 256, 16):
    96     18.1 MiB      0.0 MiB          16           s = ""
    97     18.1 MiB      0.0 MiB          19           for character in map(chr, list[i:i+16]):
    98     18.1 MiB      0.0 MiB           3               s = s + character
    99     18.1 MiB      0.0 MiB          16           string = string + s
   100     18.1 MiB      0.0 MiB           1       return string
"""

# Вариант 6:
@profile
def func6(list):
    import array
    return array.array('b', list).tostring()
func6([97, 98, 99])
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   105     18.1 MiB     18.1 MiB           1   @profile
   106                                         def func6(list):
   107     18.2 MiB      0.0 MiB           1       import array
   108     18.2 MiB      0.0 MiB           1       return array.array('b', list).tostring()
"""


# Вывод:
# Во всех 6 вариантах память использована очень оптимально.
# Кроме затрат на вызов декоратора, она больше никуда не тратится.
# Во всех 6 вариантах кода не присваиваются переменные, что очень хорошо.
# Можно заметить появление мизерных долей MiB в Варианте 6, что очень незначительно.

# В ИТОГЕ: если смотреть на оба анализа (времени и памяти) вариантов написания функции,
# то можно сделать железный вывод, что по всем показателям самый выигрышный по времени
# и по затратам на память стал Вариант 6.