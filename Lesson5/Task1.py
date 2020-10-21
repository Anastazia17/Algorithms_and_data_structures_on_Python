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

def calc():
    my_var = "Company"
    n = int(input("Введите количество предприятий: "))
    companies = namedtuple(
        my_var,
        " name profit_1_quarter profit_2_quarter profit_3_quarter profit_4_quarter")
    profit_aver = {}

    for i in range(n):
        company = companies(
            name=input("Введите название предприятия: "),
            profit_1_quarter=int(input("Введите прибыль за первый квартал: ")),
            profit_2_quarter=int(input("Введите прибыль за второй квартал: ")),
            profit_3_quarter=int(input("Введите прибыль за третий квартал: ")),
            profit_4_quarter=int(input("Введите прибыль за четвертый квартал: ")))

        profit_aver[company.name] = (
            company.profit_1_quarter + company.profit_2_quarter + company.profit_3_quarter + company.profit_4_quarter) / 4

    total_aver = 0
    for value in profit_aver.values():
        total_aver += value
    total_aver = total_aver / n

    for key, value in profit_aver.items():
        if value > total_aver:
            print(f"{key} - прибыль выше среднего.")
        elif value < total_aver:
            print(f"{key} - прибыль ниже среднего.")
        elif value == total_aver:
            print(f"{key} - средняя прибыль.")

calc()