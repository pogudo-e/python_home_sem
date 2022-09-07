#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите вещественное число: '))

# def f (n):
#     ans = 1
#     i = 1
#     arr = []
#     while n+1 > i:
#         ans = ans * i
#         arr.append(ans)
#         i += 1
#     return arr

# print(f(n))


from itertools import accumulate
import operator

n = int(input('Введите число: '))


def get_prods(n):
    return list(accumulate([x for x in range(1, n + 1)], operator.mul))

print(get_prods(n))