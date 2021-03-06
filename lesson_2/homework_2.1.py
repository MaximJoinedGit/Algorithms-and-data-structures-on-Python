# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные
# для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова
# запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он
# ввел его в качестве делителя.

while True:
    user_choice = input('Введите знак операции, которую хотите выполнить или 0 для завершения программы: ')

    # Если введен 0, то цикл завершается, если +, -, * или /, то запрашиваются числа и проводится соответствующая
    # математическая операция, а всё остальное возвращает в начало цикла с выводом соответствующего сообщения.
    if user_choice == '0':
        break
    elif user_choice != '+' and user_choice != '-' and user_choice != '*' and user_choice != '/':
        print('Такой операции нет. Повторите ввод')
    else:
        first, second = input('Введите два числа через пробел: ').split()
        first, second = float(first), float(second)
        if user_choice == '+':
            print(f'Сумма двух чисел равна {first + second}')
        elif user_choice == '-':
            print(f'Разность первого и второго чисел равна {first - second}')
        elif user_choice == '*':
            print(f'Произведение двух чисел равно {first * second:.2f}')
        elif user_choice == '/':
            if not second:
                print('Недопустимо деление на ноль! Повторите ввод')
            else:
                print(f'Деление двух чисел равно {first / second:.2f}')
