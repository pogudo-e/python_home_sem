#Реализовать алгоритм перемешивания списка. 
import random

list = list(input('Введите через пробел ваш список: ').split())

print(f'Было:  {list}')
random.shuffle(list)
print(f'Стало: {list}')
