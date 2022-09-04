# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека


import random

hello = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" \n'
    'Основные правила игры: \n'
    'Нам будет дано некоторое количество конфет, \n'
    'за один ход мы можем взять не более определённого количества, \n'
    'о котором мы с вами договоримся. \n'
    'Итак, начнём! \n')
            

def play_game(n, m, players):
    count = 0
    while n > 0:
        print(f'{players[count%2]}, твой ход')
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет, у нас всего {n} конфет')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(hello)


players = [input('Имя первого игрока: '), input('Имя второго игрока: ')]

n = int(input('Сколько конфет будем разыгрывать? '))
m = int(input('Сколько максимально будем брать конфет за один ход? '))

winer = play_game(n, m, players)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')