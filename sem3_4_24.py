# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lists = [1.1, 1.2, 3.1, 5, 10.01]
# listNum = list(map(float, input('Введите через пробел значения: ').split()))
def RList(lists):
    Newlist = []
    for num in lists:
        x = num % 1
        if x != 0:
            Newlist.append(float(x))
    result = max(Newlist) - min(Newlist)
    return str('{0:.2f}'.format(result))

print(f'{lists} => {RList(lists)}')
# print(f'{listNum} => {RList(listNum)}')
