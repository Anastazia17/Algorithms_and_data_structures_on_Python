"""
Задание 3.
Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


base_сompany = {
    'Saudi Aramco': 88211,
    'Berkshire Hathaway': 81417,
    'Apple': 55256,
    'Industrial & Commercial Bank of China': 45195,
    'Microsoft': 39240,
    'China Construction Bank': 38610,
    'JPMorgan Chase & Co.': 36431,
    'Alphabet': 34343,
    'Agricultural Bank of China': 30701,
    'Bank of America Corp.': 27430,
    'Bank of China': 27127,
    'Ping An Insurance': 21627,
    'Alibaba Group Holding': 21450
}


# 1 вариант
list_from_dictionary = list(base_сompany.items())
list_from_dictionary.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_from_dictionary[i][0], ':', list_from_dictionary[i][1])

# O(N*logN)
print('#' * 18)


# 2 вариант
def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max


print(three_max(base_сompany))

# O(N)


#Самый лучший вариант № 2, так как он менее сложный по нагрузке кода.