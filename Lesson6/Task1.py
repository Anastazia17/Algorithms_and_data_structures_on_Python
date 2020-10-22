from timeit import timeit
from functools import reduce

# Написала 6 вариантов функции,
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
import array
def func6(list):
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
# Время выполнения func1: 0.0562168 мс.

# Вариант 2:
print(timeit("""
def func2(list):
    return reduce(lambda string, item: string + chr(item), list, "")
""", """from functools import reduce"""))
# Время выполнения func2: 0.07355229999999999 мс.

# Вариант 3:
print(timeit("""
def func3(list):
    string = ""
    for character in map(chr, list):
        string = string + character
    return string
"""))
# Время выполнения func3: 0.053639099999999995 мс.

# Вариант 4:
print(timeit("""
def func4(list):
    string = ""
    lchr = chr
    for item in list:
        string = string + lchr(item)
    return string
"""))
# Время выполнения func4: 0.05180279999999998 мс.

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
# Время выполнения func5: 0.05014590000000002 мс.

# Вариант 6:
print(timeit("""
def func6(list):
    import array
    return array.array('b', list).tostring()
"""))
# Время выполнения func7: 0.048350000000000004 мс.


# Вывод:
# Вариант 1 выдал относительно неплохой результат.
# Варианты 3, 4 и 5 были немного быстрее, чем Вариант 1.
# Вариант 2 оказался самым медленными с большим отрывом.
# Вариант 6 стал самым выигрышным по скорости и довольно неплохим по читабельности кода.