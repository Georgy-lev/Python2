# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет,
# которые нужно перевернуть

from random import randint

n = int(input("Введите the number of coins: "))
count_eagle = 0
count_reshka = 0
coins = []
for i in range(n):
    coins.append(randint(1, 2))
for i in coins:
    if i == 2:
        count_eagle += 1
    else:
        count_reshka += 1
print(coins)
print(min(count_reshka, count_eagle))