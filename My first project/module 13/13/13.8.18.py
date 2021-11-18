# Реализуйте программу, которая сжимает
# последовательность символов. На вход
# подается последовательность вида: aaabbccccdaa
# Необходимо вывести строку, состоящую из символов
# и количества повторений этого символа.
# Вывод должен выглядеть как a3b2c4d1a2
text = 'aaabbccccdaa'
count = {}
for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
# print(count.items())
# dict_items([('a', 5), ('b', 2), ('c', 4), ('d', 1)])
count2 = [f'{key}, {value}' for key, value in count.items()]
# print(list(map(str, count2)))
count3 = list(map(str, count2))
count4 = ''.join(count3)
count4 = count4.replace(",", "")
count4 = count4.replace(" ", "")
count4 = count4.replace("\n", "")
print(count4)
