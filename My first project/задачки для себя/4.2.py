# Выведите все элементы списка с четными индексами.
# (т.е. первый элемент в списке, третий и т. д.).
# Подсказка: помните, что элементы в списках нумеруются,
# начиная с нуля. Используйте цикл for и переменную
# которая будет следить за номером текущего элемента
# Пример ввода:
# 1 2 3 4 5
# Вывод программы:
# 1 3 5
# Пример ввода:
# 5 2 1 7 8 9 11 17
# Вывод программы:
# 5 1 8 11
n = (input('n: ').split())
count = 0
v = ''
for i in n:
    if count % 2 == 0:
        v = v + i + str(' ')
    count += 1
print(v)