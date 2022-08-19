# Вывести на экран числа от -N до N

n = int(input('Введите число: '))

for it in range(-n, n+1):
    print(it, end = ", ")