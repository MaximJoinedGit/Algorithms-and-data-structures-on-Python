# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter = input('Введите номер буквы в алфавите, которую необходимо вывести на экран: ')

# Находим индекс самого первого элемента (первой буквы).
first_letter = ord('a')
letter = int(letter)

# По номеру буквы в алфавите определяем заданную букву, прибавив заданное число к индексу и сделав обратное
# преобразование.
print(f'Это буква {(chr(first_letter + letter - 1))}')