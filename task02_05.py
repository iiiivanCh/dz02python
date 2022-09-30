
import random

user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Оригинальный список: ", user_list)
n = len(user_list)
for i in range(n):
    j = random.randint(0, n-1)
    # print(j)
    element = user_list.pop(j)
    user_list.append(element)
print("Перемешанный список: ", user_list)
