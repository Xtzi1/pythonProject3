try:
    hour = int(input('Введите время:\t'))
except ValueError as e:
    print("Вы ввели не время!")
else:
    if 6 <= hour < 12:
        print("Утро!")
    else:
        print('Не утро')
finally:
    print('Exit')