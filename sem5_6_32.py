# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]


listNum = list(map(int, input('Введите через пробел ваш список: ').split()))

def DelDuples(List):
    li = []
    for i in List:
        if i not in li:
            li.append(i)
    return li
 
print(f'{listNum} => {DelDuples(listNum)}')