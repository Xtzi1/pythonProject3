try:
    age = int(input("How old are you?"))
    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")
except ValueError as error:
    print(error)
    print("Неправильный возраст")
else:
    print(f"You are {age} years old!")

