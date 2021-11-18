# есть два списка одинакового размера:
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1
# их надо перемножить
N = [a*b for a, b in zip (L, M)]

print(N)