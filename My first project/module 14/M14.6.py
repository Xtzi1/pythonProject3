# # 14.6.1 привести к нижнему регистру
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))
# вывести только положительные элементы
# def positive(x):
#     return x > 0
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
# print(list(result))
#
 # 14.6.2 вывести только четные элементы
# def chet(x):
#     return x % 2 == 0
# result = filter(chet, [-2, -1, 0, 1, -3, 2, -3])
# print(list(result))

# LAMBDA
# эти две функции выполняют одно и тоже — складывают два числа
# def my_function(x1, x2):  # Обычная функция
#    return x2 + x1
#
# lambda x1, x2: x2 + x1  # Анонимная функция
# # Возвести первые 10 натуральных чисел в квадрат
# list(map(lambda x: x ** 2, range(1, 11)))  # правильно
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Словари и лямбда
# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
# # Чтобы отсортировать его по ключам, нужно сделать так:
# print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
#
# # отсортировать словарь по значениям
# # у встроенной функции sortred() можно задать аргумент key,
# # который укажет, по какому ключу нужно производить сортировку.
# sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря

# 14.6.4 отсортировать их по индексу массы тела
# # Он вычисляется по формуле: рост в метрах возвести в квадрат,
# # потом массу тела в килограммах разделить на полученную цифру.
# # Из списка в предыдущем задании найдите кортеж
# # с минимальным индексом массы тела
# data = [(82, 191), (68, 174), (90, 189), (73, 179), (76, 184)]
# index = list(sorted(data, key = lambda x: x[0]/x[1]**2))
# print(index)
# # кортеж с минимальным индексом массы тела
# print(min(data, key = lambda x: x[0]/x[1]**2))

# 14.6.5 Вывести длину каждого элемента в списке
# a = ["asd", "bbd", "ddfa", "mcal"]
#
# print(list(map(lambda x: len(x), a)))
# print(list(sorted(a, key = lambda x: len(x))))

# 14.6.6 Переведите все строки из списка в верхний регистр
# a = ["это", "маленький", "текст", "обидно"]
#
# print(list(map(str.upper, a)))