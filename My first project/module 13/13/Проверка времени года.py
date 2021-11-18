try:
    a = int(input('ведите номер месяца: '))
except ValueError as e:
    print('Вы ввели не число')
else:
    if a in [3,4,5]:
     print('SPRING')
    elif a in [6,8,8]:
     print('SUMMER')
    elif a in [9,10,11]:
     print('AUTUMN')
    elif a in [12,1,2]:
     print('WINTER')
    else:
     print('Нет такого месяца!')
