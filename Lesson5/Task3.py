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

print(timeit("""
simple_lst = list("abcdefgh")
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
""",setup="from collections import deque"))
# 16.1383863 мс.


# Вывод: deque работает быстрее, чем обычный список.