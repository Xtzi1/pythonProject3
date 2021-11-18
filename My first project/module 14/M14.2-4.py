# def get_mul_func(m):
#     nonlocal_m = m
#
#     def local_mul(n):
#         return n * nonlocal_m
#
#     return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# two_mul(5)  # 5 * 2
#
# print(two_mul(5))
# Площадь круга
# PI = 3.14 # глобальная переменная
# def area_circle(r):
#     PI = 3.1415 # локальная переменная
#     print(PI)
#     return PI * (r ** 2)

# print(area_circle(7))
# # перемножатор
# def adder(*nums):
#     sum_ = 1
#     for n in nums:
#         sum_ *= n
#
#     return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6
# факториал. рекурсия
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(4))
# рекурсия. фибоначи
# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# print(rec_fibb(9))  # 55
# рекурсия. сумма чисел
# def rec_sum(n):
#     if n == 1:
#         return 1
#     return n + rec_sum(n - 1)
# print(rec_sum(6))
# # рекурсия. развернуть строку
# def rec_reverse(string):
#     if len(string) == 0:
#         return ''
#     else:
#         return string[-1] + rec_reverse(string[:-1])
# print(rec_reverse('test'))
# Вычислить сумму цифр натурального числа N
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# print(sum_digit(123))  # 6
# # возвращающую бесконечную последовательность натуральных
# # чисел. По умолчанию, она начинается с единицы и шагом 1
# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
# print(count(1, 3))
# # Создайте генератор цикла, то есть в функцию на входе
# # будет передаваться массив, например, [1, 2, 3],
# # генератор будет вечно работать возвращая 1 2 3 1 2 3…
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)
# # для примера возьмём строку
# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# # декоратор
# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
#
# print(my_function())
# # Я - оборачиваемая функция!
# # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0
# # замерить время выполнения системной функции для возведения числа
# # в степень 2 и соответствующего оператора.
# import time
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
# def pow_2():
#    return 10000000 ** 2
#
# def in_build_pow():
#    return pow(10000000, 2)
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921
#
# in_build_pow()
# # Запустилась функция <function in_build_pow at 0x7f938401b620>
# # Функция выполнилась. Время: 0.0000021458
# возвращают время работы основной функции и найдите среднее время
# # выполнения для 100 выполнений каждой функции
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")
