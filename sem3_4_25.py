# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input('Введите число: '))
i = num
result = ''
 
while i > 0:
    result = str(i % 2) + result
    i = i // 2
 
print(f'{num} => {result}')