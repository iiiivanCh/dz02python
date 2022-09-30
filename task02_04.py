# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


import random


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_list_filling(number):
    user_list = []
    for i in range(number):
        user_list.append(round(random.uniform(-number, number), 1))
    print(user_list)
    return user_list


def get_multiply_number_list(user_file):
    with open(user_file, 'r') as file:
        user_list = file.readlines()
        user_list = [i.replace('\n', '') for i in user_list]
        print(user_list)
    return user_list


def get_sum_position(position, list):
    if len(position) == 0:
        total = 0
        print('Файл file.txt пуст')
        return
    else:
        total = 1
        totalizer = 0
    for i in position:
        if int(i) < len(list):
            total *= list[int(i)]
        else:
            print(f'Позиция {int(i)} отсутствует')
            totalizer += 1
    if totalizer == 0:
        print(
            f'Произведение элементов на заданных позициях {position} = {total:.2f}')
        return
    else:
        total = 0
        print(f'Некоторые элементы отсутствуют => Произведение = {total}')


user_number = get_user_number(
    'Определяем число элементов списка. Введите целое число: ')
random_list = get_list_filling(user_number)
position = get_multiply_number_list('file.txt')
get_sum_position(position, random_list)
