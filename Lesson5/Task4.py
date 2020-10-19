"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections


print(timeit("""
NEW_DICT = {'a': 1, 'b': 2, 'c': 3}
print(NEW_DICT)
"""))

print(timeit("""
NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)
"""))