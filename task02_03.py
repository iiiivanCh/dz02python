# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_user_list_formula(number):
    user_list = []
    user_list_sum = 0
    for i in range(number):
        user_list.append((1 + 1 / (i + 1))**(i + 1))
        user_list_sum += user_list[i]
    print(f"{user_list} Сумма значений списка: {user_list_sum}")


user_number = get_user_number('Введите целое число: ')
get_user_list_formula(user_number)
