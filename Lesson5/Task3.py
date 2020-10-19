"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
from timeit import timeit

simple_lst = list("abcdefgh")
print(simple_lst)
simple_lst.append('i')
simple_lst.append('j')
simple_lst.append('k')
print(simple_lst)
simple_lst.pop()
simple_lst.pop()
simple_lst.pop()
print(simple_lst)

deq_obj = deque(simple_lst)
print(deq_obj)
deq_obj.append('i')
deq_obj.append('j')
deq_obj.append('k')
print(deq_obj)
deq_obj.pop()
deq_obj.pop()
deq_obj.pop()
print(deq_obj)


print(timeit("""
simple_lst = list("abcdefgh")
print(simple_lst)
simple_lst.append('i')
simple_lst.append('j')
simple_lst.append('k')
print(simple_lst)
simple_lst.pop()
simple_lst.pop()
simple_lst.pop()
print(simple_lst)
"""))
# Время выполнения: 18.2983061 мс.
# Почему-то словарь выводится больше 100 раз. Не понимаю почему.

print(timeit("""
deq_obj = deque(simple_lst)
print(deq_obj)
deq_obj.append('i')
deq_obj.append('j')
deq_obj.append('k')
print(deq_obj)
deq_obj.pop()
deq_obj.pop()
deq_obj.pop()
print(deq_obj)
"""))
# Здесь измерить время не получилось из-за ошибки:
# File "C:/Users/Vol4itsa/PycharmProjects/Algorithms_and_data_structures_on_Python/Lesson5/Task3.py", line 53, in <module>
#     print(timeit("""
#   File "C:\Python38\lib\timeit.py", line 233, in timeit
#     return Timer(stmt, setup, timer, globals).timeit(number)
#   File "C:\Python38\lib\timeit.py", line 177, in timeit
#     timing = self.inner(it, self.timer)
#   File "<timeit-src>", line 7, in inner
# NameError: name 'deque' is not defined


# Вывод от себя: по идее Вeque должен раотать быстрее, чем обычный список.