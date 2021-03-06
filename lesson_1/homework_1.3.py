# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randint, uniform

# Спрашиваем у пользователя что он будет вводить.
choice = input('Введите число от 1 до 3, где\n'
               '1 - Случайное целое число\n'
               '2 - Случайное вещественное число\n'
               '3 - Случайный символ\n')

if choice == '1':
    first, last = input('Введите диапазон целых чисел, из которых нужно выбрать случайное через пробел: ').split()
    first, last = int(first), int(last)

    # Если пользователь ввел числа не в порядке возрастания - мы меняем их местами.
    if first > last:
        first, last = last, first
    num = randint(first, last)
    print(f'{num} - cлучайное целое число между {first} и {last}')

elif choice == '2':
    first, last = input('Введите диапазон вещественных чисел, '
                        'из которых нужно выбрать случайное через пробел: ').split()
    first, last = float(first), float(last)

    # Если пользователь ввел числа не в порядке возрастания - мы меняем их местами.
    if first > last:
        first, last = last, first
    num = uniform(first, last)
    print(f'{num:.1f} - cлучайное вещественное число между {first} и {last}')

elif choice == '3':
    first, last = input('Введите диапазон букв (порядок алфавитный), '
                        'из которых нужно выбрать случайную через пробел: ').split()
    first, last = ord(first.lower()), ord(last.lower())

    # Если пользователь ввел буквы не в алфавитном порядке - мы меняем их местами.
    if first > last:
        first, last = last, first
    letter = randint(first, last)
    print(f'{chr(letter)} - cлучайная буква в диапазоне от {chr(first)} до {chr(last)}.')
else:
    print('Неправильный ввод.')
