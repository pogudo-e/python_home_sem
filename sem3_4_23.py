# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]




listFirst = [2, 3, 4, 5, 6]
listSecond =[2, 3, 5, 6]
listNum = list(map(int, input('Введите через пробел ваш список: ').split()))
def ParNum (lists):
    result = []
    for i in range(int(len(lists)/2 + len(lists)%2)):
        if len(lists) % 2 == 0:
            if i >= len(lists)//2:
                break
            else:
                result.append(lists[i]*lists[-(i + 1)])
        else:
            if i > len(lists)//2:
                break
            else:
                result.append(lists[i]*lists[-(i + 1)])
    return result

print(f'{listFirst} => {ParNum(listFirst)}')
print(f'{listSecond} => {ParNum(listSecond)}')
print(f'{listNum} => {ParNum(listNum)}')