#является ли хотя бы одна из переменных истинной

a = int(input('a: '))
b = int(input('b: '))

if a != 0 and b != 0:
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print(a or b)
else:
    print("Обе переменные ложные")