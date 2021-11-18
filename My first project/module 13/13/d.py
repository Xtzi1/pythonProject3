n = int(input("Введите число\n"))

while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3 + 1) // 2
    print(n)

    if n == 1:
        print("Done")
        break