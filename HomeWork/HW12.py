# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


sum_numbers = int(input("Summa of numbers: "))
multiplication_numbers = int(input("multiplication of numbers: "))
N1 = 0
N2 = 0

N1 = (sum_numbers - int((sum_numbers ** 2 - 4 * multiplication_numbers) ** 0.5)) // 2
N2 = sum_numbers - N1
if N1 and N2 >= 1000 or N1 and N2 <= 0:
    print('Задуманные числа не соответсвуют условиям задачи')
print(f'задуманные числа: {N1, N2}')