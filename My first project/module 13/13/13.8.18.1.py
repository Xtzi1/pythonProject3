# Реализуйте программу, которая сжимает
# последовательность символов. На вход
# подается последовательность вида: aaabbccccdaa
# Необходимо вывести строку, состоящую из символов
# и количества повторений этого символа.
# Вывод должен выглядеть как a3b2c4d1a2
text = 'aaabbccccdaa'
first = text[0]
count = 0
result = ''
for c in text:
    if c == first:
        count += 1
    else:
        result += first + str(count)
        first = c
        count = 1
result +=first + str(count)
print(result)