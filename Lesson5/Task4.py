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
# Время выполнения: 5.9047225 мс.
# Почему-то словарь выводится больше 100 раз. Не понимаю почему.


NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)

print(timeit("""
NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)
"""))
# Здесь измерить время не получилось из-за ошибки:
# File "C:/Users/Vol4itsa/PycharmProjects/Algorithms_and_data_structures_on_Python/Lesson5/Task4.py", line 24, in <module>
#    print(timeit("""
#  File "C:\Python38\lib\timeit.py", line 233, in timeit
#    return Timer(stmt, setup, timer, globals).timeit(number)
#  File "C:\Python38\lib\timeit.py", line 177, in timeit
#    timing = self.inner(it, self.timer)
#  File "<timeit-src>", line 7, in inner
# NameError: name 'collections' is not defined

# Вывод от себя: по идее OrderedDict должен раотать быстрее, чем обычный словарь.
