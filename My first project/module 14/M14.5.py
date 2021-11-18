# # функция для решения линейного уравнения
# def linear_solve(a, b):
#  if a:
#     return b/a
#  elif not a and not b:
#     return 'Бесконечное число корней'
#  else:
#     return 'Нет корней'
# print(linear_solve(2, 9))
# print(linear_solve(0,0))
# # квадратные уравнения
# def discriminant(a,b,c):
#     return b**2 - 4 * a * c
# def quadratic_solve(a,b,c):
#     if discriminant(a,b,c) < 0:
#         return 'Нет корней'
#     elif discriminant(a,b,c) == 0:
#         x = - b / (2 * a)
#         return f'Корень равен {x}'
#     else:
#         x1 = (-b - (discriminant(a,b,c)**0.5))/2*a
#         x2 = (-b + (discriminant(a,b,c)**0.5))/2*a
#         return f'Корни х1={x1}, х2 ={x2}'
# print(quadratic_solve(4,5,1))
# # квадратные уравнения
# def discriminant(a,b,c):
#     return b**2 - 4 * a * c
# def quadratic_solve(a,b,c):
#     if discriminant(a,b,c) < 0:
#         return 'Нет корней'
#     elif discriminant(a,b,c) == 0:
#         x = - b / (2 * a)
#         return f'Корень равен {x}'
#     else:
#         x1 = (-b - (discriminant(a,b,c)**0.5))/2*a
#         x2 = (-b + (discriminant(a,b,c)**0.5))/2*a
#         return f'Корни х1={x1}, х2 ={x2}'
# print(quadratic_solve(4,5,1))
# L = list(map(float, input('аргументы функции: ').split()))
# print(quadratic_solve(L[0], L[1], L[2]))
# print(quadratic_solve(*L))
# # 14.5.9 минимальный элемент списка
# def rec_min(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < rec_min(L[1:]) else rec_min(L[1:])
# print(rec_min([2,3,5,6]))
# #14.5.10 зеркально развернуть строку
# def rec_mirror(L):
#     if len(L) == 0:
#         return ''
#     return L[-1] + rec_mirror(L[:-1])
# print(rec_mirror('lkj'))
# #14.5.10 зеркально развернуть число без нулей
# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a//10, res * 10 + a % 10)
# print(mirror(345))
