# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from operator import iadd


def get_user_number(str_1):
    while True:
        try:
            num = float(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def get_sum_number(number):
    sum_number = 0
    for i in str(number):
        if i != "-" and i != ".":
            sum_number += int(i)
    print(f"{number} -> {sum_number}")


user_number = get_user_number("Введите вещественное число: ")
get_sum_number(user_number)
