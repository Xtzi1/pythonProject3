# Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом
# (читается одинаково слева направо
# и справа налево).

a = str(4455544)
print(a == a[::-1])