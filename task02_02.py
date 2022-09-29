# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_list_factorial(number, count=1):
    user_list = []
    for i in range(1, number + 1):
        count *= i
        user_list.append(count)
    print(f'N = {number}, тогда {user_list}', end=' т.е. ')


def get_list_multiply(number, count=1):
    user_list = []
    for i in range(1, number + 1):
        if i == 1:
            user_list.append(str(i))
        else:
            count = str(f'{count}*{i}')
            user_list.append(count)
    print(*user_list, sep=', ')


user_number = get_user_number('Введите целое число: ')
get_list_factorial(user_number)
get_list_multiply(user_number)
