# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов, сумму которых необходимо найти: '))
total = 0
elem = 1
for _ in range(n):
    total += elem
    elem *= -0.5
print(f'Сумма чисел последовательности из {n} элементов равна {total}')