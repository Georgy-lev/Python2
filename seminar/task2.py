# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

n1 = 20
n2 = 21
n3 = 22

print(n1 % 2 + n1 // 2 + n2 % 2 + n2 // 2 + n3 % 2 + n3 // 2)

