"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""

def recurs(num, new_num=0):

    if num == 0:
        return new_num
    else:
        new_num = (new_num * 10) + (num % 10)
        num = num // 10
        return recurs(num, new_num)

try:
    num = int(input("Введите число: "))
    print(f"Перевернутое число: {recurs(num)}")
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь!")