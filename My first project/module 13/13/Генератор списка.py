#квадраты только от нечетных чисел

squares = [i**2 for i in range(1,11) if i % 2 == 1]
print(squares)