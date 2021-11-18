
a = int(input('insert a: '))
if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
    print('Охуенное число: ', a)
else:
    print("TAAKOE", a)