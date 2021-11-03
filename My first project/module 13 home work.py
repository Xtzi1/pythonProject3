print('При покупке более трех билетов, скидка 10%!')
try:
    tickets = int(input('Сколько нужно билетов? Ответ: '))
    if tickets <= 0:
        print('Неверное значение')
except ValueError as error:
    print("Неверный ввод")
sum = 0
c1 = 990
c2 = 1390
for ticket in range(tickets):
    print('Сколько лет владельцу билета?')
    age = int(input('Введите возраст: '))
    if age < 18:
        sum += 0
    if 18 <= age < 25:
        sum += c1
    if 25 <= age:
        sum += c2
if tickets > 3:
    sum = sum*0.9
    print(f'Сумма со скидкой 10%: {sum} рублей')
else:
    print(f'Сумма покупки: {sum} рублей')