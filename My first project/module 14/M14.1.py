#def print_2_add_2():
#    print(2+2)
#    ...
#print_2_add_2()
#def hello_word():
#    print('Hello world!')
#    ...
#hello_word()
# объявили функцию для подсчета количества символов в неком абстрактном тексте
#def char_frequency(text):
#   text = text.lower()
#   text = text.replace(" ", "")
#   text = text.replace("\n", "")

#   count = {}  # для подсчета символов и их количества
#   for char in text:
#       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#           count[char] += 1
#       else:
#           count[char] = 1
#
#   for char, cnt in count.items():
#       print(f"Символ {char} встречается {cnt} раз")
# функция, которая возводит любое число в степень n
# # по умолчанию, в квадрат
# def pow_func(base, n=2):
#    print(base ** n)
#
# pow_func(3)  # 9
# pow_func(5, 3)  # 125
#проверяет, является ли число n делителем числа a
# def chek_num(a, n):
#    if a % n == 0:
#       print("OK")
#    else:
#       print("ostatok")
# chek_num(4,2)
# chek_num(5,2)
# печатает «обратную лесенку» следующего типа
# # n = 3
# # ***
# # **
# # *
# def reverse_stair(n):
#  for i in range(n, 0, -1):
#     print('*'*i)
# reverse_stair(4)
# Возведение в степень
# def pow_func(base, n=2):
#    inside_result = base ** n
#    return inside_result
# print(pow_func(3))
# # можем присвоить этот результат некоторой
# # переменной и использовать это значение
# # вне тела функции.
# outside_result = pow_func(3)
# print(outside_result)
# # возвращать количество делителей числа а
# def check_all_num(a):
#     count = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             count += 1
#     return count
#
# print(check_all_num(6))
# # проверяет, является ли данная строка палиндромом
# # или нет, и возвращает результат проверки
# def check_palindrome(text):
#     text = text.lower()
#     text = text.replace(' ', '')
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
# print(check_palindrome('А роза упала на лапу Азора'))
