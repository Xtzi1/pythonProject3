try:
    a = int(input('Введите целое число: '))
except ValueError as e:
    print('Вы ввели неверное число')
else:
    print(f'Вы ввели {a}')
finally:
    print('Выход из программы')