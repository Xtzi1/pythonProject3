# Напишите программу, которая определяет и выводит
# значение второго по величине элемента в последовательности
# натуральных чисел, которая завершается числом 0.
# Подсказка: второй по величине элемент в этой
# последовательности - элемент, который будет наибольшим,
# если из последовательности удалить одно вхождение
# наибольшего элемента.
# Пример ввода:
# 4
# 6
# 5
# 7
# 8
# 0
# Вывод программы:
# 7
i = int(input('Введите число: '))
counter = 0
max = 0
premax = 0
while i:
    counter += 1
    if i > max:
        premax = max
        max = i
    elif premax < i < max:
        premax = i
    i = int(input('Введите число: '))
print(f'Наибольшее введенное число: {max}')
print(f'Второе наибольшее введенное число: {premax}')