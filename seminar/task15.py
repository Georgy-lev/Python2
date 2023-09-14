# Пользователь вводит число n - количесво
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число = это масса соответствующего арбуза

from random import randint

amount = int(input())
weight = []
for i in range(amount):
    weight.append(randint(1, 10))

max = 0
min = 10
for i in weight:
    if i > max:
        max = i
    else:
        if i < min:
            min = i
print(f"минимальное число: {min} максимальное число: {max}")
print(weight)