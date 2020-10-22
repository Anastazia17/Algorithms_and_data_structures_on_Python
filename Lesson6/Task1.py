from timeit import timeit
from functools import reduce

# Написала 7 вариантов функции,
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
import string
def func6(list):
    return string.joinfields(map(chr, list), "")

# Вариант 7:
import array
def func7(list):
     return array.array('b', list).tostring()


# Делаем замеры:

# Вариант 1:
print(timeit("""
def func1(list):
    string = ""
    for item in list:
        string = string + chr(item)
    return string
"""))
# Время выполнения func1: 0.0505908 мс.

# Вариант 2:
print(timeit("""
def func2(list):
    return reduce(lambda string, item: string + chr(item), list, "")
""", """from functools import reduce"""))
# Время выполнения func2: 0.07919649999999999 мс.

# Вариант 3:
print(timeit("""
def func3(list):
    string = ""
    for character in map(chr, list):
        string = string + character
    return string
"""))
# Время выполнения func3: 0.0463914 мс.

# Вариант 4:
print(timeit("""
def func4(list):
    string = ""
    lchr = chr
    for item in list:
        string = string + lchr(item)
    return string
"""))
# Время выполнения func4: 0.05482039999999999 мс.

# Вариант 5:
print(timeit("""
def func5(list):
    string = ""
    for i in range(0, 256, 16):
        s = ""
        for character in map(chr, list[i:i+16]):
            s = s + character
        string = string + s
    return string
"""))
# Время выполнения func5: 0.053390999999999966 мс.

# Вариант 6:
print(timeit("""
import string
def func6(list):
    return string.joinfields(map(chr, list), "")
"""))
# Время выполнения func6: 0.18010710000000002 мс.

# Вариант 7:
print(timeit("""
import array
def func7(list):
     return array.array('b', list).tostring()
"""))
# Время выполнения func7: 0.1709 мс.


# Вывод:
# Вариант 1 изначально выдал неплохой результат.
# Варианты 4 и 5 были немного медленнее, чем Вариант 1.
# Варианты 2, 6 и 7 оказались самыми медленными с большим отрывом.
# Вариант 3 стал самым выигрышным по скорости и довольно неплохим по читабельности кода.