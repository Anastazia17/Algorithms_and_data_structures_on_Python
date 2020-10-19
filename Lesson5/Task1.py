"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple
from collections import Counter


COMPANY1 = namedtuple('Resume', 'name profit_1_quarter profit_2_quarter profit_3_quarter profit_4_quarter')

RESUME_PARTS1 = COMPANY1(
    name='Рога',
    profit_1_quarter='235',
    profit_2_quarter='345634',
    profit_3_quarter='55',
    profit_4_quarter='235'
)
print(RESUME_PARTS1)


COMPANY2 = namedtuple('Resume', 'name profit_1_quarter profit_2_quarter profit_3_quarter profit_4_quarter')

RESUME_PARTS2 = COMPANY2(
    name='Копыта',
    profit_1_quarter='345',
    profit_2_quarter='34',
    profit_3_quarter='543',
    profit_4_quarter='34'
)
print(RESUME_PARTS2)


OBJ = Counter([COMPANY1])
print(OBJ)

OBJ = Counter([COMPANY2])
print(OBJ)