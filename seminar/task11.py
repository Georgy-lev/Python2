# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

A = int (input("Введите число: "))
first_element, second_element, current = 0, 1, 1
count = 2
while current < A:
    current = first_element + second_element
    first_element = second_element
    second_element = current
    count+=1

if current == A:
    print(f"Элемент фибоначчи {count}")
else:
    print(-1)