# Запишите условие, которое является истинным,
# когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия
# и не пытаться упростить их.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if ((a < 45) and (b >= 45) and (c >= 45)) or\
    ((c < 45) and (a >= 45) and (b >= 45)) or\
    ((b < 45) and (c >= 45) and (a >= 45)):
    print('есть число меньше 45 и одно')
else:
    print('Числа меньше 45 нет или больше одного')