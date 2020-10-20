"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
from timeit import timeit

NEW_DICT = {'a': 1, 'b': 2, 'c': 3}
print(NEW_DICT)

print(timeit("""
NEW_DICT = {'a': 1, 'b': 2, 'c': 3}
print(NEW_DICT)
"""))
# Время выполнения: 5.1771441 мс.
# Почему-то словарь выводится больше 100 раз. Не понимаю почему.


NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)

print(timeit("""
NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)
""", "import collections"))
# Время выполнения: 6.9047955000000005 мс.

# Вывод: по идее OrderedDict должен работать быстрее, чем обычный словарь, но
# в моем случае он работал немного дольше обычного словаря.
