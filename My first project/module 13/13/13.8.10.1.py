a = int(input('insert a: '))
if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")
else:
    print("TAAKOE", a)