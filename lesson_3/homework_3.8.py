# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = [[int(input(f'Введите значение элемента {x + 1}, строки {y + 1}: ')) for x in range(4)] for y in range(4)]
print('Полученная матрица:')

for row in matrix:
    temp_sum = 0
    for elem in row:
        temp_sum += elem
        print(f'{elem:>5}', end='')
    row.append(temp_sum)
    print(f'{row[4]:>5}')
