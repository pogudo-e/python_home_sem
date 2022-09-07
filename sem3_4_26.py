# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


num = int(input('Введите число: '))


# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# def rever(lis):
#     data2 = []
#     count = 1
#     for n in lis:
#         if count % 2 == 0:
#             data2.append(-n)
#         else:
#             data2.append(n)
#         count += 1
#     data2.reverse()
#     data2.append(0)
#     return data2

# data = list(fibonacci(num))
# print(rever(data) + data)

def fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = fibonacci(num)
print(fibonacci(num))
print(fibo_nums.index(0))